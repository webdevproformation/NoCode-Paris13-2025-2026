import re
import pytest
from playwright.sync_api import expect

REGISTER_PATH = "/register"

def goto_register(page, base_url):
    page.goto(f"{base_url}{REGISTER_PATH}")
    # Optionnel: vérifier qu'on est bien sur la page
    expect(page).to_have_url(re.compile(r".*/register$"))

def disable_html5_validation(page):
    page.eval_on_selector("form", "form => form.noValidate = true")


def fill_register_form(page, pseudo=None, email=None, password=None, confirm_password=None):
    # On utilise name=... car tes champs WTForms rendent typiquement input[name="pseudo"], etc.
    if pseudo is not None:
        page.locator('input[name="pseudo"]').fill(pseudo)
    if email is not None:
        page.locator('input[name="email"]').fill(email)
    if password is not None:
        page.locator('input[name="password"]').fill(password)

    # Si tu as un champ confirm_password
    confirm = page.locator('input[name="confirm_password"]')
    if confirm.count() > 0 and confirm_password is not None:
        confirm.fill(confirm_password)

def submit_register(page):
    # Si ton submit est un <button> ou <input type="submit"> :
    # 1) essaye bouton
    btn = page.get_by_role("button", name=re.compile("créer|create|inscription|profil", re.I))
    if btn.count() > 0:
        btn.first.click()
        return
    # 2) fallback input submit
    page.locator('input[type="submit"]').first.click()


def assert_still_on_register(page):
    # En validation KO, ton endpoint renvoie render_template(register.html) => URL reste /register
    expect(page).to_have_url(re.compile(r".*/register$"))


def assert_error_visible(page, expected_text_regex):
    # Selon ton template, les erreurs peuvent apparaître:
    # - sous le champ (invalid-feedback / w-form-fail)
    # - via flash alert
    expect(page.get_by_text(re.compile(expected_text_regex, re.I))).to_be_visible()


# -------------------------------------------------------------------
# 1) Champs vides
# -------------------------------------------------------------------

def test_register_empty_submit_shows_errors(page, base_url):
    goto_register(page, base_url)

    disable_html5_validation(page)  # ✅ disables minlength/required checks by the browser
    # ne rien remplir
    submit_register(page)

    assert_still_on_register(page)

    # Erreurs possibles (selon tes validators / messages)
    # On reste "souple": on vérifie qu'au moins 1 erreur est affichée.
    # Exemple: "This field is required." ou message FR si tu l'as custom.
    errors = page.locator("css=.invalid-feedback")
    # print(errors)
    # page.pause()

    assert errors.count() == 4

    # expect(errors).to_have_count(lambda n: n > 0)


# -------------------------------------------------------------------
# 2) Emails invalides (format)
# -------------------------------------------------------------------

@pytest.mark.parametrize("bad_email", [
    "abc", "abc@", "@test.com", "test.com", "a b@test.com", "test@",
    "test@@example.com", "test@example", "test@example..com"
])
def test_register_invalid_email_format(page, base_url, bad_email):
    goto_register(page, base_url)

    disable_html5_validation(page)  # ✅ disables minlength/required checks by the browser
    fill_register_form(page,
        pseudo="UserTest",
        email=bad_email,
        password="StrongPass!123",
        confirm_password="StrongPass!123",
    )
    submit_register(page)

    

    assert_still_on_register(page)

    # page.pause()

    # WTForms Email() sort souvent une erreur type "Invalid email address."
    # Si tu l'as en français, adapte le regex.
    error = page.get_by_text("Invalid email address.")

    assert error.count() == 1
    # assert_error_visible(page, r"email|adresse|invalid")


# -------------------------------------------------------------------
# 3) Mot de passe trop faible / trop court
# -------------------------------------------------------------------

@pytest.mark.parametrize("weak_pwd", [
    "short1!",       # trop court
    "aaaaaaaa",      # pas de majuscule/chiffre/symbole
    "Password",      # pas chiffre/symbole
    "password1",     # pas majuscule/symbole
    "PASSWORD1",     # pas minuscule/symbole
])
def test_register_weak_password_rejected(page, base_url, weak_pwd):
    goto_register(page, base_url)

    disable_html5_validation(page)  # ✅ disables minlength/required checks by the browser
    fill_register_form(page,
        pseudo="UserTest",
        email="weakpwd@example.com",
        password=weak_pwd,
        confirm_password=weak_pwd,
    )
    submit_register(page)

    assert_still_on_register(page)
    # Ton message custom peut être: "Le mot de passe doit contenir..."
    # page.pause()
    assert_error_visible(page, r"mot de passe invalide|doit contenir")

# -------------------------------------------------------------------
# 4) Confirmation mot de passe ne correspond pas
# -------------------------------------------------------------------

def test_register_password_mismatch(page, base_url):
    goto_register(page, base_url)

    disable_html5_validation(page)  # ✅ disables minlength/required checks by the browser
    fill_register_form(page,
        pseudo="UserTest",
        email="mismatch@example.com",
        password="StrongPass!123",
        confirm_password="StrongPass!124",
    )
    submit_register(page)

    assert_still_on_register(page)
    assert_error_visible(page, r"ne correspondent|match|confirmation")


# -------------------------------------------------------------------
# 5) Pseudo trop court / caractères invalides (si tu as Regexp sur pseudo)
# -------------------------------------------------------------------

@pytest.mark.parametrize("bad_pseudo", [
    "a",            # trop court (min 2)
    "    a    ",            # trop court (min 2)
    "   ",          # espaces
    "user$",        # caractère non autorisé si tu limites à A-Za-z0-9_.-
])
def test_register_invalid_pseudo(page, base_url, bad_pseudo):
    goto_register(page, base_url)

    disable_html5_validation(page)  # ✅ disables minlength/required checks by the browser

    fill_register_form(page,
        pseudo=bad_pseudo,
        email="pseudo-invalid@example.com",
        password="StrongPass!123",
        confirm_password="StrongPass!123",
    )
    submit_register(page)

    assert_still_on_register(page)
    assert_error_visible(page, r"pseudo|invalide|caract")


# -------------------------------------------------------------------
# 6) Email déjà utilisé (doublon)
# -------------------------------------------------------------------

def test_register_duplicate_email(page, base_url):
    goto_register(page, base_url)

    disable_html5_validation(page)  # ✅ disables minlength/required checks by the browser

    # 1) premier register OK
    fill_register_form(page,
        pseudo="User1",
        email="dup@example.com",
        password="StrongPass!123",
        confirm_password="StrongPass!123",
    )
    submit_register(page)

    # normalement redirect login si OK
    expect(page).to_have_url(re.compile(r".*/login$"))

    # 2) retour register, même email
    goto_register(page, base_url)

    disable_html5_validation(page)  # ✅ disables minlength/required checks by the browser
    fill_register_form(page,
        pseudo="User2",
        email="dup@example.com",
        password="StrongPass!123",
        confirm_password="StrongPass!123",
    )
    submit_register(page)

    assert_still_on_register(page)
    # Ton code backend flash: "Cet email est déjà utilisé."
    assert_error_visible(page, r"déjà utilisé|already used|utilisé")
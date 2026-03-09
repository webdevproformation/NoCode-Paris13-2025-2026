import re
import pytest
from playwright.sync_api import expect

REGISTER_PATH = "/register"

# Chaînes de "fuzz" SAFE : caractères spéciaux courants (pas de payload d'exploitation)
FUZZ_STRINGS = [
    "test'quote",
    'test"double',
    "test<tag>",
    "test&entity",
    "test;semi",
    "test--dash",
]

SENSITIVE_LEAK_PATTERNS = re.compile(
    r"(traceback|sql|syntax error|sqlite|postgres|mysql|psycopg|odbc|exception|stack trace)",
    re.I
)

def get_file_content(file_name):
    with open(file_name, 'r', encoding= 'utf8') as f:
        return [line for line in f]

def goto_register(page, base_url):
    page.goto(f"{base_url}{REGISTER_PATH}")
    expect(page).to_have_url(re.compile(r".*/register$"))

def disable_html5_validation(page):
    page.eval_on_selector("form", "form => form.noValidate = true")

def submit_register(page):
    # Support <button> ou <input type="submit">
    btn = page.get_by_role("button", name=re.compile("créer|create|inscription|profil", re.I))
    if btn.count() > 0:
        btn.first.click()
    else:
        page.locator('input[type="submit"]').first.click()

def fill(page, pseudo=None, email=None, password=None, confirm_password=None):
    if pseudo is not None:
        page.locator('input[name="pseudo"]').fill(pseudo)
    if email is not None:
        page.locator('input[name="email"]').fill(email)
    if password is not None:
        page.locator('input[name="password"]').fill(password)

    confirm = page.locator('input[name="confirm_password"]')
    if confirm.count() > 0 and confirm_password is not None:
        confirm.fill(confirm_password)

def assert_no_500_and_no_leak(page):
    # 1) pas de page d'erreur visible
    html = page.content()
    assert "500" not in html
    # 2) pas de fuite d'info type SQL/Traceback
    assert not SENSITIVE_LEAK_PATTERNS.search(html)

def assert_still_on_register(page):
    expect(page).to_have_url(re.compile(r".*/register$"))

# ---------------------------
# A) Champs vides
# ---------------------------
def test_register_empty_fields(page, base_url):
    goto_register(page, base_url)

    disable_html5_validation(page)

    submit_register(page)
    assert_still_on_register(page)
    assert_no_500_and_no_leak(page)

    # Au moins une erreur doit apparaître (selon ton template)
    errors = page.locator("css=.invalid-feedback")
    # print(errors)
    # page.pause()

    page.pause()

    assert errors.count() == 4

# ---------------------------
# B) Email invalide
# ---------------------------
@pytest.mark.parametrize("bad_email", ["abc", "abc@", "@example.com", "test.example.com", "a b@example.com"])
def test_register_invalid_email_format(page, base_url, bad_email):
    goto_register(page, base_url)

    disable_html5_validation(page)

    fill(page, pseudo="UserTest", email=bad_email, password="StrongPass!123", confirm_password="StrongPass!123")
    submit_register(page)

    assert_still_on_register(page)
    assert_no_500_and_no_leak(page)

    # Erreur email (souple)
    expect(page.get_by_text(re.compile("email|adresse|invalid|invalide", re.I))).to_be_visible()

# ---------------------------
# C) “Fuzz” sur pseudo : robustesse anti-injection (SQLi/XSS)
# ---------------------------
@pytest.mark.parametrize("fuzz", FUZZ_STRINGS)
def test_register_fuzz_pseudo_do_not_crash(page, base_url, fuzz):
    goto_register(page, base_url)

    disable_html5_validation(page)

    # on injecte des caractères spéciaux dans les champs
    fill(page,
         pseudo=f"User{fuzz}",
         email=f"user@example.com", 
         password="StrongPass!123",
         confirm_password="StrongPass!123")

    submit_register(page)

    # On attend un rejet propre (email invalide), sans crash ni fuite
    assert_still_on_register(page)
    assert_no_500_and_no_leak(page)



# ---------------------------
# C) “Fuzz” sur email : robustesse anti-injection (SQLi/XSS)
# ---------------------------
@pytest.mark.parametrize("fuzz", FUZZ_STRINGS)
def test_register_fuzz_email_do_not_crash(page, base_url, fuzz):
    goto_register(page, base_url)

    disable_html5_validation(page)

    # on injecte des caractères spéciaux dans les champs
    fill(page,
         pseudo=f"User",
         email=f"user{fuzz}@example.com",   # volontairement bizarre -> doit être rejeté par Email()
         password="StrongPass!123",
         confirm_password="StrongPass!123")

    submit_register(page)

    # On attend un rejet propre (email invalide), sans crash ni fuite
    assert_still_on_register(page)
    assert_no_500_and_no_leak(page)


@pytest.mark.parametrize("fuzz", get_file_content("tests/payload-injection-sql.txt"))
def test_register_fuzz_pseudo_do_not_crash_real_payload(page, base_url, fuzz):
    goto_register(page, base_url)

    disable_html5_validation(page)

    # on injecte des caractères spéciaux dans les champs
    fill(page,
         pseudo=f"User{fuzz}",
         email=f"user@example.com",
         password="StrongPass!123",
         confirm_password="StrongPass!123")

    submit_register(page)

    # On attend un rejet propre (email invalide), sans crash ni fuite
    assert_still_on_register(page)
    assert_no_500_and_no_leak(page)



# ---------------------------
# D) Test “anti HTML injection” minimal : si reflété, doit être encodé
# ---------------------------
def test_register_html_like_input_is_not_interpreted(page, base_url):
    goto_register(page, base_url)

    disable_html5_validation(page)

    # chaîne contenant des chevrons : si jamais c'est reflété, ça doit être affiché en texte
    marker = "User<tag>"
    fill(page,
         pseudo=marker,
         email="invalid-email",   # force une erreur -> page va réafficher le formulaire
         password="StrongPass!123",
         confirm_password="StrongPass!123")

    submit_register(page)
    assert_still_on_register(page)
    assert_no_500_and_no_leak(page)

    # Vérifie que le marqueur n'apparaît pas comme HTML réel (si jamais il est affiché)
    # On vérifie qu'il n'existe pas de noeud <tag> ajouté au DOM
    expect(page.locator("tag")).to_have_count(0)

    # Et s'il est visible dans du texte, c'est OK (encodé / rendu comme texte)
    # (ce test reste souple car ton template peut ne pas réafficher le pseudo)
# tests/test_auth_e2e.py
import re
from playwright.sync_api import expect

def test_dashboard_requires_login(page, base_url):
    page.goto(f"{base_url}/dashboard")

    # We expect redirect to /login and the flash message or heading visible
    expect(page).to_have_url(re.compile(r".*/login$"))
    # If your template shows a "Connexion" heading:
    expect(page.get_by_role("heading", name=re.compile("Connexion", re.I))).to_be_visible()


def test_register_then_login_then_dashboard(page, base_url):
    # --- Register ---
    page.goto(f"{base_url}/register")

    page.locator('input[name="pseudo"]').fill("Alice")
    page.locator('input[name="email"]').fill("alice@example.com")
    page.locator('input[name="password"]').fill("StrongPass!123")
    # If you added confirm_password in your form:
    confirm = page.locator('input[name="confirm_password"]')
    if confirm.count() > 0:
        confirm.fill("StrongPass!123")

    # Submit: could be <input type="submit" value="..."> or <button>
    # Using role "button" is recommended when possible. [3](https://playwright.dev/docs/best-practices)[4](https://bondaracademy.com/blog/playwright-locators-best-practices)
    page.get_by_role("button", name=re.compile("créer|Créer|Inscription|profil", re.I)).click()

    # After successful register, your code redirects to login
    expect(page).to_have_url(re.compile(r".*/login$"))
    expect(page.get_by_text("Compte créé avec succès", exact=False)).to_be_visible()

    # --- Login ---
    page.locator('input[name="email"]').fill("alice@example.com")
    page.locator('input[name="password"]').fill("StrongPass!123")
    page.get_by_role("button", name=re.compile("Connexion", re.I)).click()

    # Redirect to dashboard
    expect(page).to_have_url(re.compile(r".*/dashboard$"))
    # Adjust assertion to something real on your dashboard page
    # e.g. heading "Dashboard" or any known text:
    # expect(page.get_by_role("heading", name=re.compile("Dashboard", re.I))).to_be_visible()


def test_register_duplicate_email_shows_warning(page, base_url):
    # First register
    page.goto(f"{base_url}/register")
    page.locator('input[name="pseudo"]').fill("Bob")
    page.locator('input[name="email"]').fill("bob@example.com")
    page.locator('input[name="password"]').fill("StrongPass!123")
    confirm = page.locator('input[name="confirm_password"]')
    if confirm.count() > 0:
        confirm.fill("StrongPass!123")
    page.get_by_role("button", name=re.compile("créer|Créer", re.I)).click()

    # page.pause()

    # Second register with same email
    page.goto(f"{base_url}/register")
    page.locator('input[name="pseudo"]').fill("Bob2")
    page.locator('input[name="email"]').fill("bob@example.com")
    page.locator('input[name="password"]').fill("StrongPass!123")
    confirm = page.locator('input[name="confirm_password"]')
    if confirm.count() > 0:
        confirm.fill("StrongPass!123")
    page.get_by_role("button", name=re.compile("créer|Créer", re.I)).click()

    # page.pause()

    # Should stay on register and show warning flash
    expect(page.get_by_text("Cet email est déjà utilisé", exact=False)).to_be_visible()


def test_logout_redirects_to_login(page, base_url):
    # Create user + login
    page.goto(f"{base_url}/register")
    page.locator('input[name="pseudo"]').fill("Charlie")
    page.locator('input[name="email"]').fill("charlie@example.com")
    page.locator('input[name="password"]').fill("StrongPass!123")
    confirm = page.locator('input[name="confirm_password"]')
    if confirm.count() > 0:
        confirm.fill("StrongPass!123")
    page.get_by_role("button", name=re.compile("créer|Créer", re.I)).click()

    page.locator('input[name="email"]').fill("charlie@example.com")
    page.locator('input[name="password"]').fill("StrongPass!123")
    page.get_by_role("button", name=re.compile("Connexion", re.I)).click()
    expect(page).to_have_url(re.compile(r".*/dashboard$"))

    # Logout
    page.goto(f"{base_url}/logout")
    expect(page).to_have_url(re.compile(r".*/login$"))
    expect(page.get_by_text("déconnecté", exact=False)).to_be_visible()
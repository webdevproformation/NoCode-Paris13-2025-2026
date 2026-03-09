# tests/conftest.py
import threading
import pytest
from werkzeug.serving import make_server

@pytest.fixture(scope="session")
def base_url():
    """
    Starts the Flask app on a random free port and returns the base URL.
    Uses an in-memory 'users' store by patching find_user_by/add_user.
    """
    import application as myapp  

    # --- In-memory store (isolated per test) ---
    users = {}

    def fake_find_user_by(field, value):
        if field == "email":
            return users.get(value)
        return None

    def fake_add_user(user):
        users[user["email"]] = user
        return user

    # Apply patches to the module where functions are USED
    myapp.find_user_by = fake_find_user_by
    myapp.add_user = fake_add_user

    # Ensure predictable testing config
    myapp.application.config.update(
        TESTING=True,
        SECRET_KEY="test-secret-key",
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
    )

    # Start server on random port (0)
    server = make_server("127.0.0.1", 0, myapp.application)
    port = server.server_port
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    try:
        yield f"http://127.0.0.1:{port}"
    finally:
        server.shutdown()
        thread.join(timeout=2)
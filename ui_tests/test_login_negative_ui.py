import pytest
import os
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv("DB_USER")

@pytest.mark.ui
def test_wrong_password(page):
    page.goto("https://demoblaze.com")

    page.get_by_role("link", name = "Log in").click()
    page.wait_for_selector("#logInModal", state = "visible")

    page.locator("#loginusername").fill(USER_NAME)
    page.locator("#loginpassword").fill("wrong_password")
    
    page.get_by_role("button", name="Log in", exact=True).click()
    alert_text = []
    page.on("dialog", lambda dialog: [alert_text.append(dialog.message), dialog.accept()])
    
    page.wait_for_timeout(2000)
    
    assert "Wrong password." in alert_text

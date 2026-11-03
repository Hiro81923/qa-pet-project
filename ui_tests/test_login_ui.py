import pytest
import os 
from dotenv import load_dotenv

load_dotenv()


USER_NAME = os.getenv("DB_USER")  
USER_PASSWORD = os.getenv("DB_PASSWORD") 

@pytest.mark.ui
def test_successful_login(page):
    page.goto("https://demoblaze.com")
    
    page.get_by_role("link", name="Log in").click()

    page.wait_for_selector("#logInModal", state="visible")
    
    page.locator("#loginusername").fill(USER_NAME)
    page.locator("#loginpassword").fill(USER_PASSWORD)
    
    page.get_by_role("button", name="Log in").click()
    
    welcome_selector = f"text=Welcome {USER_NAME}"
    page.wait_for_selector(welcome_selector, state="visible", timeout=7000)
    
    assert page.locator(welcome_selector).is_visible()

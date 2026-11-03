import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        is_ci = os.getenv("CI") == "true"
        
        browser = p.chromium.launch(headless=is_ci)
        context = browser.new_context(
            base_url="https://demoblaze.com",
            viewport={"width": 1280, "height": 720}
        )
        yield context
        context.close()
        browser.close()

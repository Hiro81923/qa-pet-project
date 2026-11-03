import pytest

@pytest.mark.ui
def test_filter_by_laptop_category(page):
    page.goto("https://demoblaze.com")

    page.wait_for_selector(".card-title", state="visible")
    
    page.get_by_role("link", name="Laptops").click()

    page.wait_for_selector("text=Sony vaio i5", state="visible", timeout=5000)
    
    laptop_locator = page.get_by_role("link", name = "Sony vaio i5").first
    assert laptop_locator.is_visible()
    
    phone_locator = page.get_by_role("link", name = "Samsung galaxy s6").first
    phone_locator.wait_for(state="hidden", timeout=5000)
    assert not phone_locator.is_visible()
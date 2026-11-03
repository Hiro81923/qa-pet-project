import pytest

@pytest.mark.ui
def test_add_product_to_cart(page):
    page.goto("https://demoblaze.com")
    
    page.get_by_role("link", name="Samsung galaxy s6").first.click()
    
    page.get_by_role("link", name="Add to cart").click()
    page.on("dialog", lambda dialog: dialog.accept())
    
    page.get_by_role("link", name="Cart", exact=True).click()
    
    product_locator = page.locator("#tbodyid").get_by_text("Samsung galaxy s6").first
    product_locator.wait_for(state="visible", timeout=7000)
    
    assert product_locator.is_visible()

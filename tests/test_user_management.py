import time
import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

UNIQUE_USERNAME = f"krishna_qa_{int(time.time())}"
PASSWORD_DATA = "SecurePass123!"

@pytest.fixture(autouse=True)
def setup_admin_module(page):
    """Fixture to handle automatic login and navigation before every test block"""
    login_page = LoginPage(page)
    admin_page = AdminPage(page)
    
    login_page.navigate()
    login_page.login("Admin", "admin123")
    admin_page.click_admin_menu()
    yield

def test_tc01_navigate_to_admin(page):
    """Validate dashboard navigation to the Admin module"""
    assert "admin/viewSystemUsers" in page.url

def test_tc02_add_user(page):
    """Validate adding a completely new user execution flow"""
    admin_page = AdminPage(page)
    admin_page.add_new_user("m", UNIQUE_USERNAME, PASSWORD_DATA) 
    
    admin_page.search_user(UNIQUE_USERNAME)
    expect(page.get_by_role("cell", name=UNIQUE_USERNAME)).to_be_visible()
def test_tc03_search_user(page):
    """Validate finding the target user via the search grid filter"""
    admin_page = AdminPage(page)
    admin_page.search_user(UNIQUE_USERNAME)
    expect(page.get_by_role("cell", name=UNIQUE_USERNAME)).to_be_visible()

def test_tc04_and_tc05_edit_and_validate_user(page):
    """Modify user role to ESS and validate updates adhere correctly"""
    admin_page = AdminPage(page)
    admin_page.search_user(UNIQUE_USERNAME)
    admin_page.edit_user_role_to_ess()
    
    admin_page.search_user(UNIQUE_USERNAME)
    expect(page.get_by_role("cell", name="ESS")).to_be_visible()

def test_tc06_and_tc07_delete_and_verify_removal(page):
    """Remove target user and ensure data grid reads empty confirmation"""
    admin_page = AdminPage(page)
    admin_page.search_user(UNIQUE_USERNAME)
    admin_page.delete_user()
    
    admin_page.search_user(UNIQUE_USERNAME)
    expect(page.locator("span").filter(has_text="No Records Found")).to_be_visible()
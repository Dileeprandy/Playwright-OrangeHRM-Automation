class AdminPage:
    def __init__(self, page):
        self.page = page
        self.admin_menu = page.locator("span").filter(has_text="Admin").first
        self.add_button = page.get_by_role("button", name=" Add ")
        
        # Add User Form Controls
        self.user_role_dropdown = page.locator(".oxd-select-text").first
        self.employee_name_input = page.get_by_placeholder("Type for hints...")
        self.status_dropdown = page.locator(".oxd-select-text").nth(1)
        self.username_input = page.locator("label").filter(has_text="Username").locator("xpath=../following-sibling::div//input").first
        self.password_input = page.locator("label").filter(has_text="Password").locator("xpath=../following-sibling::div//input").first
        self.confirm_password_input = page.locator("label").filter(has_text="Confirm Password").locator("xpath=../following-sibling::div//input").first
        self.save_button = page.get_by_role("button", name=" Save ")

        # Search Controls
        self.search_username_input = page.locator("label").filter(has_text="Username").locator("xpath=../following-sibling::div//input").first
        self.search_button = page.get_by_role("button", name=" Search ")

        # Table Grid Actions
        self.edit_icon = page.locator(".bi-pencil-fill").first
        self.delete_icon = page.locator(".bi-trash").first
        self.confirm_delete_button = page.get_by_role("button", name=" Yes, Delete ")

    def click_admin_menu(self):
        self.admin_menu.click()
        self.add_button.wait_for(state="visible", timeout=15000)

    def add_new_user(self, employee_hint, new_username, password):
        self.add_button.click()
        self.page.wait_for_selector(".oxd-form", state="visible")
        
        self.user_role_dropdown.click()
        self.page.get_by_role("option", name="Admin").click()
        
        self.status_dropdown.click()
        self.page.get_by_role("option", name="Enabled").click()

        
        self.employee_name_input.click()
        self.employee_name_input.fill("") # Clear the box just in case
        
        self.employee_name_input.press_sequentially("a", delay=300) 
        
        self.page.wait_for_timeout(3000) 
        
        self.employee_name_input.press("ArrowDown")
        self.employee_name_input.press("Enter")

        self.username_input.fill(new_username)
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)
        
        self.save_button.click()
        self.page.wait_for_selector(".oxd-form", state="hidden", timeout=15000)
        self.page.wait_for_load_state("networkidle")

    def search_user(self, username):
        self.search_username_input.fill(username)
        self.search_button.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000) 

    def edit_user_role_to_ess(self):
        self.edit_icon.click()
        self.page.wait_for_selector(".oxd-form", state="visible")
        self.user_role_dropdown.click()
        self.page.get_by_role("option", name="ESS").click()
        self.save_button.click()
        self.page.wait_for_selector(".oxd-form", state="hidden", timeout=15000)

    def delete_user(self):
        self.delete_icon.click()
        self.confirm_delete_button.click()
        self.page.wait_for_load_state("networkidle")
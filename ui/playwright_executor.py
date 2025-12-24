from playwright.sync_api import sync_playwright

def execute_ui_test(base_url, test_case):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(base_url)

        # Example: login flow
        if "Login" in test_case["title"]:
            page.click("text=Login")
            page.fill("input[type=email]", "test@test.com")
            page.fill("input[type=password]", "Test@123")
            page.click("button[type=submit]")

            if "Logout" in page.content():
                browser.close()
                return "Pass", "Login successful"
            else:
                browser.close()
                return "Fail", "Login failed"

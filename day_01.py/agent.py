from playwright.sync_api import sync_playwright
import time

def linkedin_agent():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Open LinkedIn login
        page.goto("https://www.linkedin.com/login")
        
        # YOU manually type password here
        print("👉 Please login manually in the browser!")
        print("👉 After logging in, come back here and press ENTER")
        input()  # Waits for you to press Enter
        
        # Agent takes over after you login
        page.goto("https://www.linkedin.com/in/me/")
        print("✅ Profile loaded! Agent is ready!")
        
        time.sleep(30)
        browser.close()

linkedin_agent()

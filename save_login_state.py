from playwright.sync_api import sync_playwright
from common.auth import manual_login

def createLoginSession():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        manual_login(page)

        context.storage_state(path="login_state.json")
        browser.close()

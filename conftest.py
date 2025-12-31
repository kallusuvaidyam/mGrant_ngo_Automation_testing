import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page_manual():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture
def page_auto():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            storage_state="login_state.json"
        )
        page = context.new_page()
        page.goto(
            "https://stg.trif.mgrant.in/app/home",
            wait_until="domcontentloaded",
            timeout=60000
        )
        yield page
        context.close()
        browser.close()

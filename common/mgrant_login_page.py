def login_mGrant_NGO(page):
    page.goto("https://stg.trif.mgrant.in/admin", timeout=60000, wait_until="domcontentloaded")

    page.locator("#login_email").fill("Administrator")
    page.locator("#login_password").fill("admin@dhwani")

    page.keyboard.press("Enter")

    # dashboard load hone ka wait
    page.wait_for_url("**/app/home", timeout=60000)

def ProposalStarter(page):
  page.locator("a[title='Proposals']").wait_for(state="visible")
  page.locator("a[title='Proposals']").click()

  page.wait_for_load_state("networkidle")

  page.locator("div[number_card_name='Proposals']").wait_for(state="visible")
  page.locator("div[number_card_name='Proposals']").click()

  page.wait_for_load_state("networkidle")
  page.wait_for_timeout(1000)

  page.locator("button[data-label='Add Proposal']").wait_for(state="visible")
  page.locator("button[data-label='Add Proposal']").click()

  page.wait_for_load_state("networkidle")
  page.wait_for_timeout(1000)



def GrantStarter(page):
  page.locator("a[title='Grants']").wait_for(state="visible")
  page.locator("a[title='Grants']").click()

  page.wait_for_load_state("networkidle")

  page.locator("div[number_card_name='Total Grants']").wait_for(state="visible", timeout=10000)
  page.locator("div[number_card_name='Total Grants']").click()

  page.wait_for_load_state("networkidle")
  page.wait_for_timeout(1000)

  # page.locator("button[data-label='Add Grant']").wait_for(state="visible")
  # page.locator("button[data-label='Add Grant']").click()

  page.locator("a[data-name='D-0007MP']").wait_for(state="visible", timeout=30000)
  page.locator("a[data-name='D-0007MP']").click()

  page.wait_for_load_state("networkidle")
  page.wait_for_timeout(3000)
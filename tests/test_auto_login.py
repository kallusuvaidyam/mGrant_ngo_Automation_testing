from pages.mgrant_ngo_testing import fillProposalForm, fillGrantForm

def test_auto_logged_in_flow(page_auto):
    # fillProposalForm(page_auto)
    fillGrantForm(page_auto)

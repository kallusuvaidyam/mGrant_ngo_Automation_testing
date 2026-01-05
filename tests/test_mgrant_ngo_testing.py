from common.auth import manual_login
from pages.mgrant_ngo_testing import fillProposalForm, fillGrantForm

def test_login_mGrant_NGO(page_manual):
    manual_login(page_manual)
    # fillProposalForm(page_auto)
    fillGrantForm(page_manual)
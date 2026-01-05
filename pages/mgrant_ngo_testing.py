from pages.ngo_form_for_proposal import ngoFormDetails, ngoFormGeography, ngoFormTasks, ngoFormFiles, ngoFormNotes, ngoFormAuditLogs, ngoFormStages
from pages.mgrant_starter import ProposalStarter, GrantStarter
from pages.ngo_form_for_grant import grantFormDetails, grantFormGeographicalInformation, grantFormTimeframe, grantFormTask, grantFormBudgetAllocation, grantFormFundManagement, grantFormOutput, grantFormComplianceReporting, grantFormResourceAllocation, grantFormDocuments, grantFormAuditLogs


def fillProposalForm(page):

    ProposalStarter(page)
    

    # ========================  Canvan to List View Form   ========================
    # page.locator("button.btn.btn-default.btn-sm.ellipsis").click()
    # page.wait_for_timeout(3000)

    # page.locator("a.grey-link.dropdown-item:has-text('List View')").click()
    # page.wait_for_timeout(3000)

    # page.locator("//*[@id='page-List/Proposal/List']/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/div[3]/div/div[1]/div[1]").click()
    # page.wait_for_timeout(3000)
    # ========================  End Canvan to List View Form   ========================

    ngoFormDetails(page)
    # ngoFormGeography(page)
    # ngoFormTasks(page) # Not Complete
    # ngoFormFiles(page)
    # ngoFormNotes(page)
    # ngoFormAuditLogs(page)
    # ngoFormStages(page)
    
    page.wait_for_timeout(10000)


def fillGrantForm(page):
    GrantStarter(page)

    
    # grantFormDetails(page)
    # grantFormGeographicalInformation(page)
    # grantFormTimeframe(page)

    grantFormTask(page)# Not Complete
    # grantFormBudgetAllocation(page) # Not Complete
    # grantFormFundManagement(page) # Not Complete

    # grantFormOutput(page)
    # grantFormComplianceReporting(page)
    # grantFormResourceAllocation(page) # Not Complete
    # grantFormDocuments(page)
    # grantFormAuditLogs(page)
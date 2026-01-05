def ngoFormDetails(page):
    steps = [
        ("fill", "//*[@id='proposal-__details']/div[3]/div/div[1]/form/div[1]/div/div[2]/div[1]/div/div/input", "Amresh Yadav", 1000),
        ("fill", "//*[@id='proposal-__details']/div[3]/div/div[2]/form/div[1]/div/div[2]/div[1]/input", "Test Project", 1000),
        ("fill", "//*[@id='proposal-__details']/div[3]/div/div[3]/form/div[1]/div/div[2]/div[1]/div/div/input", "Amresh Yadav", 1000),
        ("select", "//*[@id='proposal-__details']/div[3]/div/div[4]/form/div/div/div[2]/div[1]/select", "Fresh", 1000),
        ("fill", "//*[@id='proposal-__details']/div[3]/div/div[2]/form/div[2]/div/div[2]/div[1]/input", "100000", 1000),

        ("click", ".section-head.collapsible.collapsed:has-text('Donor Information')", None, False, 1000),
        ("fill", "input[data-fieldname='donor']", "Shakti Corporate Foundation", 1000),
        ("click", "//*[@id='proposal-__details']/div[6]/div[1]", None, False, 1000),

        ("fill", "//*[@id='proposal-__details']/div[6]/div[2]/div[1]/form/div[1]/div/div[2]/div[1]/div/div/input", "Test Practice", 1000),
        ("fill", "//*[@id='proposal-__details']/div[6]/div[2]/div[2]/form/div/div/div[2]/div[1]/div/div/input", "Health", 1000),

        ("click", "//*[@id='proposal-__details']/div[7]/div[2]/div[1]/form/div/div/div[2]/div[1]/button", None, False, 2000),
        ("click", "button:has-text('Link')", None, False, 1000),
        ("fill", "input[placeholder='Attach a web link']", "https://picsum.photos/200/300", 2000),
        ("click", "button.btn-modal-primary", None, False, 2000),

        ("click", "input[data-fieldname='mou_verified']", None, False, 3000),
        ("click", "button[data-label='Save']", None, False, 3000),
    ]

    perform_steps(page, steps)


def ngoFormGeography(page):
    steps = [
        ("click", "#proposal-geography_tab-tab", None, False, 3000),
        ("select", "select[data-fieldname='lowest_geography_level']", "District", 1000),

        ("click", ".form-check-label:has-text('Bihar')", None, False, 1000),
        ("click", ".form-check-label:has-text('Delhi')", None, False, 1000),

        ("click", "//*[@id='proposal-geography_tab']/div[2]/div/div/form/div/div/div/div/div[1]/div/div[3]/button", None, False, 1000),
        ("refresh", None, None, 3000),

        ("click", "button.btn.btn-primary:has-text('Next')", None, False, 1000),
        ("click", "label.form-check-label:has-text('Bhojpur')", None, False, 1000),
        ("click", "label.form-check-label:has-text('New Delhi')", None, False, 1000),
        ("click", "button.btn.btn-primary:has-text('Save')", None, False, 1000),
    ]

    perform_steps(page, steps)


def ngoFormTasks(page):
    steps = [
        ("click", "#proposal-tasks_tab-tab", None, False, 3000),
        ("click", "button.btn.btn-secondary.btn-sm:has-text('Add row')", None, False, 3000),

        ("fill", "input[data-fieldname='custom_title']", "Test Task", 1000),
        ("select", "select[data-fieldname='priority']", "High", 1000),
        ("date", "date", "28-12-2025", 1000),
        ("fill", "input[data-fieldname='allocated_to']", "abhi@gmail.com", 1000),
        ("quill", "div[data-fieldname='description'] .ql-editor", "Testing Task", 1000),

        ("click", "button[class='btn btn-primary btn-sm btn-modal-primary']", None, False, 3000),
        ("click", "#refresh_button", None, False, 3000),
    ]

    perform_steps(page, steps)


def ngoFormFiles(page):
    steps = [
        ("click", "button#proposal-gallery_tab-tab:has-text('Files')", None, False, 3000),
        ("click", "button#customUploadButton", None, False, 2000),
        ("click", "button[data-fieldname='file']", None, False, 1000),

        ("click", "button.btn.btn-file-upload:has-text('Link')", None, 1000),
        ("fill", "input[placeholder='Attach a web link']", "https://picsum.photos/200/300", 2000),

        ("click", ".modal.fade.show .modal-dialog .modal-content .modal-footer .standard-actions button.btn.btn-primary.btn-sm.btn-modal-primary:has-text('Upload') >> nth=0", None, True, 1000),
    ]

    perform_steps(page, steps)


def ngoFormNotes(page):
    steps = [
        ("click", "#proposal-note_tab-tab", None, False, 3000),
        ("fill", "input[placeholder='Give your note a title']", "Test Title", 1000),
        ("click", "div[data-placeholder='Start writing from here']", "Testing", False, 1000),
        ("click", "//*[@id='create-form']/button", None, True, 1000),
    ]

    perform_steps(page, steps)



def ngoFormAuditLogs(page):
    steps = [
        ("click", "#proposal-timeline_tab-tab", None, False, 3000),
        ("select", "//*[@id='custom-component-timeline']/div[1]/div/select", "Proposal", 1000),
    ]

    perform_steps(page, steps)


def ngoFormStages(page):
    steps = [
        ("click", "#proposal-__details-tab", None, False, 3000),

        ("click", ".stepper__item:has-text('Initial outreach')", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Yes')", None, False, 3000),

        ("click", ".stepper__item:has-text('Initial Conversation/ Pitching')", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Yes')", None, False, 3000),

        ("click", ".stepper__item:has-text('Conecpt note WIP')", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Yes')", None, False, 3000),

        ("click", ".stepper__item:has-text('Proposal WIP') >> nth=0", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Yes')", None, False, 3000),

        ("click", ".stepper__item:has-text('Concept note submitted')", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Yes')", None, False, 3000),

        ("click", ".stepper__item:has-text('Proposal submitted')", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Yes')", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog.msgprint-dialog .modal-content .modal-header .modal-actions .btn.btn-modal-close.btn-link", None, False, 3000),
        ("date", "submission_date", "27-12-2025", 3000),
        ("click", "button[data-label='Save']", None, False, 3000),

        ("click", ".stepper__item:has-text('Concept approved, proposal WIP')", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Yes')", None, False, 3000),

        ("click", ".stepper__item:has-text('Proposal under donor review')", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Yes')", None, False, 3000),

        ("click", ".stepper__item:has-text('Concept note under donor review')", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Yes')", None, False, 3000),

        ("click", ".stepper__item:has-text('Negotiation')", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Yes')", None, False, 3000),

        ("click", ".stepper__item:has-text('Proposal Approved')", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Yes')", None, False, 3000),

        ("click", ".stepper__item:has-text('Due Diligence')", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Yes')", None, False, 3000),

        ("click", ".stepper__item:has-text('MoU Signing WIP')", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Yes')", None, False, 3000),

        ("click", ".stepper__item:has-text('MoU Signed 👍')", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Yes')", None, False, 3000),
        ("click", ".modal.fade.show .modal-dialog.msgprint-dialog .modal-content .modal-header .modal-actions .btn.btn-modal-close.btn-link", None, False, 3000),
        ("date", "start_date", "27-12-2025", 1000),
        ("date", "end_date", "28-12-2025", 1000),
        ("fill", "input[data-fieldname='sanctioned_amount']", "100000", 1000),
        ("click", "button[data-label='Save']", None, False, 3000),


    ]

    perform_steps(page, steps)




def perform_steps(page, steps):
    for step in steps:

        # backward compatible unpacking
        if len(step) == 4:
            action, selector, value, wait = step
            force = False
        elif len(step) == 5:
            action, selector, value, force, wait = step
        else:
            raise ValueError(f"Invalid step format: {step}")

        # actions
        if action == "fill":
            fill_enter(page, selector, value, wait)

        elif action == "date":
            set_date_field(page, selector, value, wait)

        elif action == "click":
            click(page, selector, value, force, wait)

        elif action == "select":
            select_option(page, selector, value, wait)

        elif action == "quill":
            fill_quill_editor(page, selector, value, wait)

        elif action == "refresh":
            refresh_page(page, selector, value, wait)

        elif action == "pause":
            pause_page(page)





def fill_enter(page, selector, value, wait=1000):
    page.locator(selector).wait_for(state="visible")
    page.locator(selector).fill(value)
    page.wait_for_timeout(wait)
    page.keyboard.press("Tab")
    page.wait_for_timeout(wait)


def set_date_field(page, fieldname, date_value, wait=500):
    # readonly remove
    page.evaluate(
        """(fname) => {
            const el = document.querySelector(
                `input[data-fieldname="${fname}"]`
            );
            if (el) el.removeAttribute("readonly");
        }""",
        fieldname
    )

    selector = f'input[data-fieldname="{fieldname}"]'

    page.locator(selector).wait_for(state="visible")
    page.fill(selector, date_value)
    page.press(selector, "Tab")   # Frappe change/blur trigger
    page.wait_for_timeout(wait)



def click(page, selector, value=None, force=False, wait=1000):
    locator = page.locator(selector).first

    locator.wait_for(state="visible")

    if value:
        locator.fill(value)

    if force is True:
        locator.click(force=True)
    else:
        locator.click()

    page.wait_for_timeout(wait)




def click_text(page, text, wait=1000):
    page.get_by_text(text).click()
    page.wait_for_timeout(wait)


def fill_quill_editor(page, selector, text, wait=1000):
    editor = page.locator(selector).first
    editor.wait_for(state="visible", timeout=60000)
    editor.click()
    page.keyboard.type(text)
    page.wait_for_timeout(wait)


def select_option(page, selector, value, wait=1000):
    page.locator(selector).wait_for(state="visible")
    page.locator(selector).select_option(value)
    page.wait_for_timeout(wait)


def refresh_page(page, selector=None, value=None, wait=1000):
    page.reload()
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(wait)


def pause_page(page):
    page.pause()


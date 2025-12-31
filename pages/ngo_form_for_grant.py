from .ngo_form_for_proposal import perform_steps

def grantFormDetails(page):
    steps = [
        ("fill", "//*[@id='grant-details_tab']/div[3]/div[2]/div[1]/form/div/div/div[2]/div[1]/input", "Test Grant", 1000),
        ("date", "start_date", "30-12-2025", 1000),
        ("date", "end_date", "31-12-2025", 1000),
        ("fill", "input[data-fieldname='custom_tri_spoc']", "abc123", 1000),
        ("fill", "input[data-fieldname='custom_type_of_practice']", "Test Practice", 1000),
        ("fill", "input[data-fieldname='custom_thematic_areas']", "Health", 1000),
        ("fill", "input[data-fieldname='custom_kpis']", "Test", 1000),
        ("fill", "textarea[data-fieldname='grant_description']", "Test Objective", 1000),
        ("fill", "input[data-fieldname='donor']", "Aashray Trust", 1000),
        ("fill", "input[data-fieldname='total_planned_budget']", "100000", 1000),
        ("click", "button[data-label='Save']", None, False, 3000),
    ]

    perform_steps(page, steps)



def grantFormGeographicalInformation(page):
    steps = [
        ("click", "button#grant-geographical_information_tab-tab", None, False, 1000),
        ("select", "select[data-fieldname='geo_select']", "District", 1000),
        ("click", ".form-check-label:has-text('Bihar')", None, False, 1000),
        ("click", ".form-check-label:has-text('Delhi')", None, False, 1000),
        ("click", "button.btn.btn-primary:has-text('Next')", None, False, 1000),
        ("click", "label.form-check-label:has-text('Bhojpur')", None, False, 1000),
        ("click", "label.form-check-label:has-text('New Delhi')", None, False, 1000),
        ("click", ".button-group .btn.btn-primary:has-text('Save')", None, False, 1000),
    ]

    perform_steps(page, steps)



def grantFormTimeframe(page):
    steps = [
        ("click", "button#grant-timeframe_tab-tab", None, False, 1000),
        ("click", "div[data-original-title='Edit']", None, False, 1000),
    ]

    perform_steps(page, steps)



def grantFormTask(page):
    steps = [
        ("click", "button#grant-tasks_tab-tab", None, False, 1000),
        ("click", "div[data-fieldname='task_planner'] #footer-element #create-button-container", None, False, 1000),
        ("click", ".modal.fade.show .modal-dialog.modal-lg .modal-content .modal-body.ui-front .form-layout .form-page .form-section.visible-section .section-body .form-column.col-sm-6 .form-group.frappe-control.input-max-width .checkbox .input-area", None, False, 1000),
        ("fill", "input[data-fieldname='task_name']", "Test Task", 1000),
        ("click", "div.modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Create')", None, False, 1000),

        # ("click", "div[data-fieldname='task_planner'] #footer-element #create-button-container", None, False, 1000),
        # ("fill", "div[data-fieldname='task_name'] .form-group.horizontal .control-input-wrapper .control-input input[data-fieldname='task_name']", "Testing", 1000),
        # ("fill", "input[data-fieldname='parent_task_name']", "Test Task", 1000),
        # ("select", ".modal.fade.show .modal-dialog.modal-lg .modal-content .modal-body.ui-front .form-layout .form-page .form-section.visible-section .section-body div[data-fieldname='column_break_pfce'] form .frappe-control.input-max-width .form-group.horizontal .control-input-wrapper .control-input.flex.align-center .select[data-fieldname='frequency']", "Monthly", 1000),
        # ("select", "div[data-fieldname='task_name'] .form-group.horizontal .control-input-wrapper .control-input select[data-fieldname='day']", "Start of the month", 1000),
        # ("click", "div.modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Create')", None, False, 1000),


        # ("click", "div[data-fieldname='tasks'] #footer-element #create-button-container", None, False, 1000),
        # ("fill", "input[data-fieldname='custom_title']", "Test Task", 1000),
        # ("click", "div.modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Create')", None, False, 1000),
    ]

    perform_steps(page, steps)



def grantFormBudgetAllocation(page):
    steps = [
        ("click", "#grant-budget_tab-tab", None, True, 3000),
        ("click", "#sva-datatable-wrapper-budget #footer-element #create-button-container #create:has-text('Add row')", None, False, 1000),
        ("fill", ".modal.fade.show .modal-dialog.modal-xl .modal-content .modal-body.ui-front .form-layout .form-page .form-section.hide-border.visible-section div[data-fieldname='column_break_gyjd'] .frappe-control.input-max-width .control-input-wrapper .control-input .link-field.ui-front .awesomplete input[data-fieldname='budget_head']", "PERSONNEL PROGRAM", False, 1000),
        ("fill", "textarea[data-fieldname='item_name']", "PERSONNEL PROGRAM", False, 1000),
        ("fill", "input[data-fieldname='custom_volac_id']", "abc123", False, 1000),
        ("fill", "input[data-fieldname='planned_amount']", "100", False, 1000),
        ("click", ".modal.fade.show .modal-dialog.modal-xl .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Create')", None, False, 1000),
    ]

    perform_steps(page, steps)



def grantFormFundManagement(page):
    steps = [
        ("click", "#grant-tranche_tab-tab", None, True, 3000),
        ("click", "#create:has-text('Add row')", None, False, 1000),
        ("fill", "input[data-fieldname='tranche_description']", "Test Tranche", False, 1000),
        ("date", "planned_due_date", "31-12-2025", False, 1000),
        ("fill", "input[data-fieldname='total_funds_planned']", "1000", False, 1000),
        # ("fill", "input[data-fieldname='planned_amount']", "100", False, 1000),
        ("click", ".modal.fade.show .modal-dialog.modal-lg .modal-content .modal-footer .standard-actions .btn.btn-primary.btn-sm.btn-modal-primary:has-text('Create')", None, False, 3000),

        # ("click", "span[data-toggle='dropdown']", None, True, 5000),

    ]

    perform_steps(page, steps)
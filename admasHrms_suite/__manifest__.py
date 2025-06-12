{
    "name": "Admas HRMS Suite",
    "version": "18.0.1.0.0",
    "category": "Human Resources",
    "summary": "Central Launcher for Admas HRMS Corporate Modules",
    "description": "Unified Corporate HRMS Suite for AdmasTech.",
    "author": "AdmasTech",
    "website": "https://www.admas.sa",
    "license": "LGPL-3",
    "application": true,
    "installable": true,
    "auto_install": false,
    "depends": [
        "admasHrms_core",
        "admasHrms_employee_creation_from_user",
        "admasHrms_employee_documents_expiry",
        "admasHrms_salary_advance",
        "admasHrms_loan",
        "admasHrms_loan_accounting",
        "hr_employee_updation",
        "hr_resignation",
        "hr_leave_request_aliasing",
        "hr_payroll_community",
        "hr_payroll_account_community",
        "hr_multi_company",
        "hr_reminder"
    ],
    "data": [
        "views/menu.xml"
    ]
}
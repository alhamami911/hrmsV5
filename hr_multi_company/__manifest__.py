{
    "name": "hr_multi_company",
    "version": "18.0.1.0.0",
    "category": "Generic Modules/Human Resources",
    "summary": "Enables Multi-Company",
    "description": "This module enables multi company features",
    "author": "AdmasTech Techno solutions,Open HRMS",
    "company": "AdmasTech",
    "maintainer": "AdmasTech",
    "website": "https://www.openhrms.com",
    "depends": [
        "hr",
        "hr_contract",
        "hr_payroll_community",
        "hr_expense",
        "hr_attendance",
        "hr_employee_transfer"
    ],
    "data": [
        "security/multi_company_security.xml",
        "views/hr_attendance_views.xml",
        "views/hr_payslip_run_views.xml",
        "views/hr_salary_rule_category_views.xml"
    ],
    "images": [
        "static/description/banner.png"
    ],
    "license": "LGPL-3",
    "installable": true,
    "auto_install": false,
    "application": false
}
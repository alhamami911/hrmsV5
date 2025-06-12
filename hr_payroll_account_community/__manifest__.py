{
    "name": "hr_payroll_account_community",
    "version": "18.0.1.0.0",
    "category": "Human Resources",
    "summary": "Odoo 17 HR Payroll, payroll, Odoo17 Payroll, Odoo Payroll, \n     Payroll, Odoo17 Payslips, Employee Payroll, HR Payroll,Odoo17, Odoo17 HR, \n     odoo hr,odoo17, Accounting,Odoo Apps",
    "description": " This module helps you to manage payroll and \n     accounting.",
    "test": [
        "../account/test/account_minimal_test.xml"
    ],
    "author": "AdmasTech",
    "company": "AdmasTech",
    "maintainer": "AdmasTech",
    "website": "https://www.openhrms.com",
    "depends": [
        "hr_payroll_community",
        "account"
    ],
    "data": [
        "views/hr_contract_views.xml",
        "views/hr_payslip_run_views.xml",
        "views/hr_payslip_views.xml",
        "views/hr_salary_rule_views.xml"
    ],
    "images": [
        "static/description/banner.jpg"
    ],
    "license": "LGPL-3",
    "installable": true,
    "auto_install": false,
    "application": false
}
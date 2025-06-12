{
    "name": "hr_resignation",
    "version": "18.0.1.0.0",
    "category": "Human Resources",
    "summary": "Manages the resignation process of the employees",
    "description": "This module helps to create and approve/reject employee\n     resignation requests",
    "author": "AdmasTech",
    "company": "AdmasTech",
    "maintainer": "AdmasTech",
    "website": "https://www.admas.sa",
    "depends": [
        "hr_employee_updation"
    ],
    "data": [
        "security/hr_resignation_security.xml",
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "data/ir_cron_data.xml",
        "views/hr_employee_views.xml",
        "views/hr_resignation_views.xml"
    ],
    "live_test_url": "https://youtu.be/BorJthxY_VI",
    "images": [
        "static/description/banner.jpg"
    ],
    "license": "LGPL-3",
    "installable": true,
    "auto_install": false,
    "application": true
}
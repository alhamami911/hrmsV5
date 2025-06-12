{
    "name": "hr_leave_request_aliasing",
    "version": "18.0.1.0.0",
    "category": "Human Resources",
    "summary": "Automated Leave Request generation from Incoming Emails.",
    "description": "This module simplifies leave request creation by \n     seamlessly generating requests from incoming emails, making the process \n     efficient, saving time, and enhancing employee experience.",
    "live_test_url": "https://youtu.be/jQFAP20k_Wc",
    "author": "AdmasTech Techno solutions, Open HRMS",
    "company": "AdmasTech",
    "maintainer": "AdmasTech",
    "website": "https://www.openhrms.com",
    "depends": [
        "hr_holidays"
    ],
    "data": [
        "data/mail_alias_data.xml",
        "views/res_config_settings_views.xml"
    ],
    "images": [
        "static/description/banner.jpg"
    ],
    "license": "LGPL-3",
    "installable": true,
    "auto_install": false,
    "application": false
}
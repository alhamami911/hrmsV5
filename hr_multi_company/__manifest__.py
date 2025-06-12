# -*- coding: utf-8 -*-
#############################################################################
#    A part of Open HRMS Project <https://www.openhrms.com>
#
#    AdmasTech Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY AdmasTech Technologies(<https://www.admas.sa>)
#    Author: AdmasTech(<https://www.admas.sa>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'Open HRMS Multi-Company',
    'version': '18.0.1.0.0',
    'category': 'Generic Modules/Human Resources',
    'summary': """Enables Multi-Company""",
    'description': 'This module enables multi company features',
    'author': 'AdmasTech Techno solutions,Open HRMS',
    'company': 'AdmasTech',
    'maintainer': 'AdmasTech',
    'website': "https://www.openhrms.com",
    'depends': ['hr', 'hr_contract', 'hr_payroll_community',
                'hr_expense', 'hr_attendance', 'hr_employee_transfer'],
    'data': [
        'security/multi_company_security.xml',
        'views/hr_attendance_views.xml',
        'views/hr_payslip_run_views.xml',
        'views/hr_salary_rule_category_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}

# -*- coding: utf-8 -*-
#############################################################################
#    A part of OpenHRMS Project <https://www.openhrms.com>
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
from odoo import fields, models


class HrEmployeeRelation(models.Model):
    """Model to store employee relationship information."""

    _name = 'hr.employee.relation'
    _description = 'HR Employee Relation'

    name = fields.Char(string="Relationship",
                       help="Relationship with the employee")

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
from odoo import fields, models


class HrAttendance(models.Model):
    """ Adding company in hr_attendance model """
    _inherit = 'hr.attendance'

    company_id = fields.Many2one(comodel_name='res.company',
                                 string='Company',
                                 copy=False, readonly=True,
                                 help="Company of the attendance.",
                                 default=lambda self: self.env.user.company_id)

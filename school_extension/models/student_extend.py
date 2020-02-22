# -*- coding: utf-8 -*-

from odoo import models, fields


class StudentExtend(models.Model):
    _inherit = 'student.student'

    address = fields.Char(string='Address')

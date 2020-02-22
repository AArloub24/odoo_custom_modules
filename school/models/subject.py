# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api
from datetime import datetime


class Subject(models.Model):
    _name = 'school.subject'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    subject_code = fields.Char(string='Code', required=True)
    name = fields.Char(string='Name', required=True)
    subject_unit = fields.Integer(string='Unit', required=True)
    active = fields.Boolean(String="Status", default=True)

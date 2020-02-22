# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api
from datetime import datetime


class Student(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    student_dob = fields.Date(string="Date of Birth")

    @api.onchange('student_dob')
    def _onchange_birth_date(self):
        """Updates age field when birth_date is changed"""
        if self.student_dob:
            d1 = datetime.strptime(str(self.student_dob), "%Y-%m-%d")

            d2 = datetime.today()
            self.age = relativedelta(d2, d1).years

    age = fields.Integer(string="Age")
    image = fields.Binary(string='Image')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')

    student_blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nationality')

    active = fields.Boolean(String="Status", default=True)

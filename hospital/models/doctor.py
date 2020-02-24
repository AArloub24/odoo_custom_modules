# -*- coding: utf-8 -*-
from datetime import datetime

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    # age generator
    @api.onchange('doctor_dob')
    def _onchange_birth_date(self):
        """Updates age field when birth_date is changed"""
        if self.doctor_dob:
            d1 = datetime.strptime(str(self.doctor_dob), "%Y-%m-%d")

            d2 = datetime.today()
            self.doctor_age = relativedelta(d2, d1).years

    doctor_age = fields.Integer(string='Age', track_visibility="always")

    # age checker
    @api.constrains('doctor_age')
    def check_age(self):
        for rec in self:
            if rec.doctor_age < 0:
                raise ValidationError(("Age can't be a negative number"))

    # open appointment function
    @api.multi
    def open_doctor_appointment(self):
        return {
            'name': ('Appointments'),
            'domain': [('doctor_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    # get appointment count
    def get_appointment_count(self):
        self.appointment_count = self.env['hospital.appointment'].search_count([('doctor_id', '=', self.id)])

    # generating doctor id
    @api.model
    def create(self, vals):
        if vals.get('doctor_id_seq', ('New') == ('New')):
            vals['doctor_id_seq'] = self.env['ir.sequence'].next_by_code('hospital.doctor.sequence') or ('New')
        result = super(HospitalDoctor, self).create(vals)
        return result

    name = fields.Char(string='Name', required=True, track_visibility="always")
    doctor_dob = fields.Date(string="Date of Birth", track_visibility="always")
    doctor_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
    notes = fields.Text(string='Notes', track_visibility="always")
    image = fields.Binary(string="Image", track_visibility="always")
    active = fields.Boolean(String="Status", default=True, track_visibility="always")
    doctor_email = fields.Char(String="Email", track_visibility="always")
    doctor_address = fields.Char(String="Address", track_visibility="always")
    country = fields.Many2one('res.country', string='Country', track_visibility="always")
    doctor_id = fields.Char(String="Test", track_visibility="always")
    doctor_id_seq = fields.Char(string='Doctor ID', required=True, copy=False, readonly=True,
                                 index=True, default=lambda self: ('New'), track_visibility="always")
    appointment_count = fields.Integer(String="Appointment Count", compute=get_appointment_count)

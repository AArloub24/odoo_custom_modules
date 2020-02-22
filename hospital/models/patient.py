# -*- coding: utf-8 -*-
from datetime import datetime

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    # age generator
    @api.onchange('patient_dob')
    def _onchange_birth_date(self):
        """Updates age field when birth_date is changed"""
        if self.patient_dob:
            d1 = datetime.strptime(str(self.patient_dob), "%Y-%m-%d")

            d2 = datetime.today()
            self.patient_age = relativedelta(d2, d1).years

    patient_age = fields.Integer(string='Age', track_visibility="always")

    # age checker
    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age < 0:
                raise ValidationError(("Age can't be a negative number"))

    # open appointment function
    @api.multi
    def open_patient_appointment(self):
        return {
            'name': ('Appointments'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    # get appointment count
    def get_appointment_count(self):
        self.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])

    # generating patient id
    @api.model
    def create(self, vals):
        if vals.get('patient_id_seq', ('New') == ('New')):
            vals['patient_id_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or ('New')
        result = super(HospitalPatient, self).create(vals)
        return result

    # # generating age_group
    @api.onchange('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'

                elif 18 <= rec.patient_age < 60:
                    rec.age_group = 'adult'

                else:
                    rec.age_group = 'senior'

    name = fields.Char(string='Name', required=True, track_visibility="always")
    patient_dob = fields.Date(string="Date of Birth", track_visibility="always")
    patient_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
    notes = fields.Text(string='Notes', track_visibility="always")
    image = fields.Binary(string="Image", track_visibility="always")
    active = fields.Boolean(String="Status", default=True, track_visibility="always")
    patient_email = fields.Char(String="Email", track_visibility="always")
    patient_address = fields.Char(String="Address", track_visibility="always")
    country = fields.Many2one('res.country', string='Country', track_visibility="always")
    patient_id = fields.Char(String="Test", track_visibility="always")
    patient_id_seq = fields.Char(string='Patient ID', required=True, copy=False, readonly=True,
                                 index=True, default=lambda self: ('New'), track_visibility="always")
    age_group = fields.Selection([('minor', 'Minor'), ('adult', 'Adult'), ('senior', 'Senior')], String="Age Group",
                                 compute="set_age_group", track_visibility="always")
    appointment_count = fields.Integer(String="Appointment Count", compute=get_appointment_count)

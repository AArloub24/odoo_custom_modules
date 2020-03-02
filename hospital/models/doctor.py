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
    doctor_fee = fields.Integer(String="Doctor Fee", track_visibility="always", required=True)
    specialization_lines = fields.One2many('hospital.specialization.lines', 'doctor_id',
                                           string="Specialization Lines")


class HospitalDoctorSpecialization(models.Model):
    _name = 'hospital.specialization.lines'
    _description = 'Doctor Specialization Record'
    _rec_name = 'name'

    name = fields.Many2one('hospital.specialization', required=True, string='Specialization')
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor ID")

    subspeciality = fields.Selection(
        [('none', 'None'), ('OG', 'Obstetrics & Gynecology '), ('FM', 'Family Medicine'), ('IM', 'Internal Medicine '),
         ('path', 'Pathology '), ('GS', 'General Surgery ')],
        string='Subspeciality' ,track_visibility="always")
    age_range = fields.Selection(
        [('all', 'All'), ('adult', 'Adult'), ('pediatric', 'Pediatric'), ('neonatal', 'Neonatal'),
         ('geriatic', 'Geriatic')],
        string='Age Range of Patients', track_visibility="always")
    DT = fields.Selection(
        [('both', 'Both'), ('D', 'Diagnostic'), ('T', 'Therapeutic'), ],
        string='Diagnostic or Therapeutic Specialty', track_visibility="always")
    SI = fields.Selection([('both', 'Both'), ('neither', 'Neither'), ('S', 'Surgical'), ('I', 'Internal'), ],
                          string='Surgical or Internal Specialty', track_visibility="always")
    OT = fields.Selection([('both', 'Both'), ('neither', 'Neither'), ('md', 'Multidisciplinary'), ('OB', 'Organ-Based'),
                           ('TB', 'Technique-Based'), ],
                          string='Organ-based or Technique-based Specialty', track_visibility="always")

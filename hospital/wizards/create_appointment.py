# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HospitalDoctor(models.TransientModel):
    _name = 'create.appointment'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, track_visibility="always")
    patient_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender',
                                      related="patient_id.patient_gender", track_visibility="always")
    patient_age = fields.Integer('Age', related="patient_id.patient_age", track_visibility="always")
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True, track_visibility="always")
    doctor_fee = fields.Integer('Doctor Fee', related="doctor_id.doctor_fee", track_visibility="always")

    notes = fields.Text(String='Prescriptions', track_visibility="always")
    pharmacy_notes = fields.Text(String='Pharmacy Notes', track_visibility="always")

# -*- coding: utf-8 -*-


from odoo import models, fields, api
from datetime import datetime


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    # generating patient id
    @api.model
    def create(self, vals):
        if vals.get('name', ('New') == ('New')):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence') or ('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    name = fields.Char(String="Appointment ID", required="True", copy=False, readonly=True, index=True,
                       default=lambda self: ('New'), track_visibility="always")
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True, track_visibility="always")
    doctor_fee = fields.Integer('Doctor Fee', related="doctor_id.doctor_fee", track_visibility="always")
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, track_visibility="always")
    patient_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender',
                                      related="patient_id.patient_gender", track_visibility="always")
    patient_age = fields.Integer('Age', related="patient_id.patient_age", track_visibility="always")
    notes = fields.Text(String='Prescriptions', track_visibility="always")
    pharmacy_notes = fields.Text(String='Pharmacy Notes', track_visibility="always")

    # get date today for default of appointment date
    def get_date_today(self):
        return datetime.today().strftime('%Y-%m-%d')

    appointment_date = fields.Date(String='Date', required=True, default=get_date_today, track_visibility="always")
    active = fields.Boolean(String="Status", default=True, track_visibility="always")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], 'Status', readonly=True, track_visibility='onchange', default='draft')




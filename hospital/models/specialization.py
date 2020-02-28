from odoo import models, fields, api


class HospitalSpecialization(models.Model):
    _name = 'hospital.specialization'
    _description = 'Specialization Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'specialization_name'

    specialization_name = fields.Char(String="Specialization", required="True", track_visibility="always")
    sub_speciality = fields.Selection(
        [('none', 'None'), ('OG', 'Obstetrics & Gynecology '), ('FM', 'Family Medicine'), ('IM', 'Internal Medicine '),
         ('path', 'Pathology '), ('GS', 'General Surgery ')],
        string='Subspeciality', track_visibility="always")
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
    active = fields.Boolean(String="Status", default=True, track_visibility="always")

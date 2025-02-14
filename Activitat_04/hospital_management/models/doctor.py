from odoo import models, fields

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'
    
    name = fields.Char('Name', required=True)
    registration_number = fields.Char('Registration Number', required=True)
    patient_ids = fields.Many2many('hospital.patient', string='Patients', through='hospital_diagnosis')
    license_number = fields.Char('License Number') 


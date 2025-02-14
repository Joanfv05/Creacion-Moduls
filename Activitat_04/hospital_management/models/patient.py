from odoo import models, fields

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient'
    
    name = fields.Char('Name', required=True)
    symptoms = fields.Text('Symptoms')
    doctor_ids = fields.Many2many('hospital.doctor', string='Doctors', through='hospital_diagnosis')


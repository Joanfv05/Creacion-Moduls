from odoo import models, fields

class Diagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnosis'
    
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    diagnosis = fields.Text('Diagnosis')


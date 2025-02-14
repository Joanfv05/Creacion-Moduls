from odoo import models, fields

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'

    name = fields.Char(string="Nom de la consulta", required=True)
    patient_id = fields.Many2one('hospital.patient', string="Pacient", required=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Metge", required=True)
    diagnosis = fields.Text(string="Diagnòstic")
    date = fields.Date(string="Data de l'atenció", required=True, default=fields.Date.context_today)


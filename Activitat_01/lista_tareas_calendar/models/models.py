from odoo import models, fields

class ListaTareas(models.Model):
    _name = 'lista_tareas.lista'
    _description = 'Lista de Tareas Calendar'

    tarea = fields.Char(string="Tarea")
    prioridad = fields.Selection([
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja')
    ], string="Prioridad")
    urgente = fields.Boolean(string="Urgente")
    realizada = fields.Boolean(string="Realizada")
    date_start = fields.Datetime(string="Fecha de Inicio")
    date_end = fields.Datetime(string="Fecha de Fin")


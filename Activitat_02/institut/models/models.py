from odoo import models, fields

# Modelo: Cicle Formatiu
class CicleFormatiu(models.Model):
    _name = 'cicle.formatiu'
    _description = 'Cicle Formatiu'

    name = fields.Char(string="Nom del Cicle", required=True)
    description = fields.Text(string="Descripció")
    module_ids = fields.One2many('modul', 'cicle_id', string="Mòduls")

# Modelo: Mòdul
class Modul(models.Model):
    _name = 'modul'
    _description = 'Mòdul de Formació'

    name = fields.Char(string="Nom del Mòdul", required=True)
    cicle_id = fields.Many2one('cicle.formatiu', string="Cicle Formatiu")
    professor_id = fields.Many2one('professor', string="Professor")
    alumne_ids = fields.Many2many('alumne', string="Alumnes Matriculats")

# Modelo: Alumne
class Alumne(models.Model):
    _name = 'alumne'
    _description = 'Alumne del Institut'

    name = fields.Char(string="Nom de l'Alumne", required=True)
    module_ids = fields.Many2many('modul', string="Mòduls Matriculats")

# Modelo: Professor
class Professor(models.Model):
    _name = 'professor'
    _description = 'Professor del Institut'

    name = fields.Char(string="Nom del Professor", required=True)
    module_ids = fields.One2many('modul', 'professor_id', string="Mòduls que Imparteix")

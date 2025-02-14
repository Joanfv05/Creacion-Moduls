from odoo import models, fields

class Socio(models.Model):

    _name = 'biblioteca.socio'
    _description = 'Socios de la Biblioteca'

    name = fields.Char(string="Nombre", required=True)
    surname = fields.Char(string="Apellido", required=True)
    identifier = fields.Char(string="Identificador Único", required=True)

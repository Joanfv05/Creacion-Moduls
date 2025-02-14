from odoo import models, fields, api

class Ejemplar(models.Model):
    _name = 'biblioteca.ejemplar'
    _description = 'Ejemplares de Cómics'

    comic_id = fields.Many2one('biblioteca.comic', string="Cómic", required=True)
    socio_id = fields.Many2one('biblioteca.socio', string="Socio")
    loan_date = fields.Date(string="Fecha de Préstamo")
    return_date = fields.Date(string="Fecha Prevista de Devolución")

    @api.constrains('loan_date', 'return_date')
    def _check_dates(self):
        for record in self:
            if record.loan_date and record.loan_date > date.today():
                raise ValidationError("La fecha de préstamo no puede ser posterior a hoy.")
            if record.return_date and record.return_date < date.today():
                raise ValidationError("La fecha de devolución no puede ser anterior a hoy.")

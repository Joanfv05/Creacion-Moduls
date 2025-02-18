# -*- coding: utf-8 -*-
from odoo import models, fields, api

# Definimos el modelo de datos
class lista_tareas(models.Model):
    # Nombre y descripción del modelo de datos
    _name = 'lista_tareas.lista'
    _description = 'Modelo de la lista de tareas'
    
    # Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    # se necesite un nombre, se usará el atributo tarea
    _rec_name = "tarea"
    
    # Elementos de cada fila del modelo de datos
    # Los tipos de datos a usar en el ORM son
    # https://www.odoo.com/documentation/17.0/developer/reference/addons/orm.html#fields
    
    tarea = fields.Char()
    prioridad = fields.Integer()
    
    # Indicamos que este valor es computado y se computará con la función "_value_urgente"
    # Con store=True indicamos que, pese a ser computado, cada vez que se compute se
    # guardará en la base de datos. Esto se hace para que podamos utilizar el campo en
    # búsquedas, filtrados y ordenaciones
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()
    
    # Este es un ejemplo de "valor computado". Este cómputo depende de la variable prioridad.
    # La dependencia se indica mediante el decorador
    @api.depends('prioridad')
    # Función para calcular el valor de urgente.
    # Recibe "self", que se refiere al modelo completo (no a un registro solo)
    def _value_urgente(self):
        # Para cada registro... (recordemos, self es el modelo, no un solo registro)
        for record in self:
            # Si la prioridad es mayor que 10, se considera urgente; en otro caso no lo es
            if record.prioridad > 10:
                record.urgente = True
            else:
                record.urgente = False


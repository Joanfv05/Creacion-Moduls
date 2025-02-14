# -*- coding: utf-8 -*-
{
    'name': "Lista de tareas Kanban",
    'summary': """
        Sencilla Lista de tareas
    """,
    'description': """
        Sencilla lista de tareas utilizadas para crear un nuevo módulo con un nuevo modelo
        de datos.
    """,
    'author': "Joan Ferre",
    'website': "https://github.com/Joanfv05",
    
    # Indicamos que es una aplicación
    'application': True,
    
    # En la siguiente URL se indica qué categorías pueden usarse:
    # https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/ir_module_category_data.xml
    # Vamos a utilizar la categoría 'Productivity'
    'category': 'Productivity',
    
    'version': '0.1',
    
    # Indicamos lista de módulos necesarios para que este funcione correctamente
    # En este ejemplo solo depende del módulo "base"
    'depends': ['base'],
    
    # Esto siempre se carga
    'data': [
        # El primer fichero indica la política de acceso del modelo
        # Más información en:
        # https://www.odoo.com/documentation/17.0/es/developer/howtos/rdtraining/05_securityintro.html
        'security/ir.model.access.csv',
        
        # Cargamos las vistas y las plantillas
        'views/views.xml',
    ],
}


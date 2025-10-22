# -*- coding: utf-8 -*-
from openerp import models, fields, api

class New(models.Model):
    _name = 'odoo8_module_news_distefano.new'
    _description = 'Modelo de Noticias Internas de RRHH - Distefano'

    start_date = fields.Date(
        string='Fecha de Inicio',
        required=True,
        default=fields.Date.context_today
    )
    end_date = fields.Date(
        string='Fecha de Fin'
    )
    description = fields.Text(
        string='Descripción de la noticia',
        required=True
    )
    
    employee_id = fields.Many2one(
        'hr.employee',
        string='Empleado',
        required=True,
        help='Empleado asociado.'
    )
    
    type_id = fields.Many2one(
        'odoo8_module_news_distefano.type',
        string='Tipo de noticia',
        required=True,
        help='Tipo de noticia.'
    )

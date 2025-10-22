# -*- coding: utf-8 -*-
from openerp import models, fields, api

class News(models.Model):
    _name = 'news.report'
    _description = 'Registro de Noticias Internas Distefano'

    start_date = fields.Date(string='Fecha de Inicio', required=True, default=fields.Datetime.now)
    end_date = fields.Date(string='Fecha de Fin') 
    report_description = fields.Text(string='Descripción del reporte', required=True, default='Nueva noticia interna')
    worker = fields.Text(string='Temporal solo nombre del trabajador', required=True, default='Nombre del trabajador')
    type_id = fields.Many2one('news.type', string='Tipo de noticia', required=True)

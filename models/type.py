# -*- coding: utf-8 -*-
from openerp import models, fields, api

class NewsType(models.Model):
    _name = 'news.type'
    _description = 'Tipo de Noticias Internas Distefano'

    name = fields.Char(string='Nombre', required=True)

from openerp import models, fields, api

class Type(models.Model):
    _name = 'odoo8_module_news_distefano.type'
    _description = 'Modelo de tipos de Noticias Internas RRHH - Distefano'

    name = fields.Char(
        string='Tipo de noticia',
        required=True
    )
    
    news_ids = fields.One2many(
        'odoo8_module_news_distefano.new',
        'type_id',
        string='Noticias'
    )

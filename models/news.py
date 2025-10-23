# -*- coding: utf-8 -*-
from openerp import models, fields, api

class News(models.Model):
    _name = 'news.report'
    _description = 'Registro de Noticias Internas Distefano'

    creation_date = fields.Datetime(string='Fecha de Creación', required=True, default=fields.Datetime.now)
    start_date = fields.Date(string='Fecha de Inicio', required=True, default=fields.Datetime.now)
    end_date = fields.Date(string='Fecha de Fin') 
    report_description = fields.Text(string='Descripción del reporte', required=True)
    type_id = fields.Many2one('news.type', string='Tipo de noticia', required=True)

    worker_id = fields.Many2one('hr.employee', string='Empleado', required=True)
    worker_name = fields.Char(string='Nombre', related='worker_id.name', store=True, readonly=True)
    worker_email = fields.Char(string='Correo', related='worker_id.work_email', store=True, readonly=True)
    worker_phone = fields.Char(string='Teléfono', related='worker_id.work_phone', store=True, readonly=True)
    worker_department = fields.Many2one('hr.department', string='Departamento', related='worker_id.department_id', store=True, readonly=True)
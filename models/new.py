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
    
    employee_email = fields.Char(
        string='Email',
        related='employee_id.work_email',
        store=False,
        readonly=True
    )

    employee_job = fields.Many2one(
        'hr.job',
        string='Cargo', 
        related='employee_id.job_id', 
        store=False, 
        readonly=True
    )
    
    employee_department = fields.Many2one(
        'hr.department', 
        string='Departamento', 
        related='employee_id.department_id', 
        store=False, 
        readonly=True
    )
    
    type_id = fields.Many2one(
        'odoo8_module_news_distefano.type',
        string='Tipo de noticia',
        required=True,
        help='Tipo de noticia.'
    )

    name = fields.Char(
        string='Código',
        compute='generate_code',
        store=True
    )

    @api.depends('employee_id', 'start_date')
    def generate_code(self):
        for rec in self:
            if rec.employee_id:
                nombres = rec.employee_id.name.split()
                iniciales = ''.join([n[0].upper() for n in nombres])
            else:
                iniciales = 'NN'
            year = ''
            if rec.start_date:
                year = str(fields.Date.from_string(rec.start_date).year)

            rec.name = "{}{}".format(iniciales, year)
            
    @api.model
    def create(self, vals):
        if not vals.get('end_date') and vals.get('start_date'):
            vals['end_date'] = vals['start_date']
        return super(New, self).create(vals)

    @api.multi
    def write(self, vals):
        for rec in self:
            if not vals.get('end_date') and ('start_date' in vals or not rec.end_date):
                vals['end_date'] = vals.get('start_date', rec.start_date)
        return super(New, self).write(vals)

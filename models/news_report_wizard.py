# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.exceptions import Warning
import base64
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from cStringIO import StringIO
from datetime import datetime
from reportlab.platypus import Image
from reportlab.lib.units import inch
from openerp.modules import get_module_resource

class NewsReportWizard(models.TransientModel):
    _name = 'odoo8_module_news_distefano.news_report_wizard'
    _description = 'Wizard para generar reporte PDF de noticias internas'

    new_id = fields.Many2one(
        'odoo8_module_news_distefano.new',
        string='Registro base',
        required=True,
        help='Selecciona el registro de noticia desde el cual generar el reporte'
    )

    
    file_data = fields.Binary('PDF data', readonly=True)
    file_name = fields.Char('Archivo', size=64)
    
    @api.model
    def default_get(self, fields_list):
        """Selecciona automáticamente el registro base desde donde se abrió el wizard"""
        res = super(NewsReportWizard, self).default_get(fields_list)
        active_id = self._context.get('active_id')
        if active_id:
            res['new_id'] = active_id
        return res

    
    @api.multi
    def generate_news_pdf(self):
        """Genera el PDF de noticias agrupadas por mes para un empleado"""
        for wizard in self:
            news_base = wizard.new_id
            employee = news_base.employee_id
            news_records = self.env['odoo8_module_news_distefano.new'].search(
                [('name', '=', news_base.name)],
                order='start_date'
            )
            
            buffer = StringIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
            elements = []
            styles = getSampleStyleSheet()
            
            logo_path = get_module_resource('odoo8_module_news_distefano', 'static', 'description', 'logo.png')
            logo = Image(logo_path)

            max_width = 6 * inch   # ancho máximo
            max_height = 1.5 * inch  # altura máxima que consideramos profesional

            if logo.imageWidth > max_width or logo.imageHeight > max_height:
                ratio = min(max_width / logo.imageWidth, max_height / logo.imageHeight)
                logo.drawWidth = logo.imageWidth * ratio
                logo.drawHeight = logo.imageHeight * ratio
            else:
                logo.drawWidth = logo.imageWidth
                logo.drawHeight = logo.imageHeight

            logo.hAlign = 'CENTER'
            elements.append(logo)
            elements.append(Spacer(1, 12))
            
            title_style = styles['Heading1']
            title_style.alignment = 1  # Centrado
            title = Paragraph("REPORTE DE NOTICIAS INTERNAS", title_style)
            elements.append(title)
            elements.append(Spacer(1, 12))
            
            info_style = styles['BodyText']
            employee_info = [
                "<b>Empleado:</b> {0}".format(employee.name),
                "<b>Código:</b> {0}".format(news_base.name),
                "<b>Cargo:</b> {0}".format(employee.job_id.name if employee.job_id else "N/A"),
                "<b>Departamento:</b> {0}".format(employee.department_id.name if employee.department_id else "N/A"),
                "<b>Generado el:</b> {0}".format(datetime.now().strftime('%d/%m/%Y'))
            ]

            for info in employee_info:
                elements.append(Paragraph(info, info_style))
            elements.append(Spacer(1, 20))
            
            news_by_month = {}
            for news in news_records:
                if news.start_date:
                    month_year = fields.Date.from_string(news.start_date).strftime("%B %Y")
                    if month_year not in news_by_month:
                        news_by_month[month_year] = []
                    news_by_month[month_year].append(news)
            
            sorted_months = sorted(news_by_month.keys(), key=lambda x: datetime.strptime(x, "%B %Y"))
            
            for month in sorted_months:
                month_title = Paragraph("<b>{0}</b>".format(month), styles['Heading2'])
                elements.append(month_title)
                elements.append(Spacer(1, 10))
                
                data = [['Fecha Inicio', 'Fecha Fin', 'Tipo', 'Descripción']]
                for news in news_by_month[month]:
                    data.append([
                        news.start_date or "",
                        news.end_date or "",
                        news.type_id.name or "",
                        news.description or ""
                    ])
                
                table = Table(data, colWidths=[80, 80, 120, 220])
                table.setStyle(TableStyle([
                    ('GRID', (0,0), (-1,-1), 1, colors.black),
                    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#001F4D")),
                    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0,0), (-1,0), 10),
                    ('BOTTOMPADDING', (0,0), (-1,0), 6),
                    ('BACKGROUND', (0,1), (-1,-1), colors.white),
                    ('TEXTCOLOR', (0,1), (-1,-1), colors.black),
                    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                    ('FONTSIZE', (0,1), (-1,-1), 9),
                ]))
                
                elements.append(table)
                elements.append(Spacer(1, 20))
            
            doc.build(elements)
            pdf_data = buffer.getvalue()
            buffer.close()
            
            wizard.write({
                'file_data': base64.b64encode(pdf_data),
                'file_name': 'Noticias_{0}_{1}.pdf'.format(employee.name.replace(" ", "_"), datetime.now().strftime("%Y%m%d"))
            })
        
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'odoo8_module_news_distefano.news_report_wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'target': 'new',
        }

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
                    ('BACKGROUND', (0,0), (-1,0), colors.beige),
                    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0,0), (-1,0), 10),
                    ('BOTTOMPADDING', (0,0), (-1,0), 6),
                    ('BACKGROUND', (0,1), (-1,-1), colors.beige),
                    ('FONTSIZE', (0,1), (-1,-1), 9),
                    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.black])
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

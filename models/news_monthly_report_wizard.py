# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.exceptions import Warning
import base64
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from cStringIO import StringIO
from datetime import datetime
from reportlab.platypus import Image
from reportlab.lib.units import inch
from openerp.modules import get_module_resource
import calendar

class NewsMonthlyReportWizard(models.TransientModel):
    _name = 'odoo8_module_news_distefano.news_monthly_report_wizard'
    _description = 'Wizard para generar reporte PDF mensual por empleado'

    month = fields.Selection(
        [
            ('1', '01 - Enero'),
            ('2', '02 - Febrero'),
            ('3', '03 - Marzo'),
            ('4', '04 - Abril'),
            ('5', '05 - Mayo'),
            ('6', '06 - Junio'),
            ('7', '07 - Julio'),
            ('8', '08 - Agosto'),
            ('9', '09 - Septiembre'),
            ('10', '10 - Octubre'),
            ('11', '11 - Noviembre'),
            ('12', '12 - Diciembre')
        ],
        string='Mes',
        required=True,
        default=lambda self: str(datetime.now().month)
    )


    year = fields.Integer(
        string='Año',
        required=True,
        default=lambda self: datetime.now().year
    )
    file_data = fields.Binary('Archivo PDF', readonly=True)
    file_name = fields.Char('Archivo', size=64)

    @api.multi
    def generate_monthly_employee_news_pdf(self):
        """Genera PDF mensual agrupando noticias por empleado con su información"""
        for wizard in self:
            month_int = int(wizard.month)
            year_int = wizard.year

            last_day = calendar.monthrange(year_int, month_int)[1]
            news_records = self.env['odoo8_module_news_distefano.new'].search([
                ('start_date', '>=', '{}-{:02d}-01'.format(year_int, month_int)),
                ('start_date', '<=', '{}-{:02d}-{:02d}'.format(year_int, month_int, last_day))
            ], order='employee_id, start_date')

            if not news_records:
                raise Warning("No hay noticias para el mes seleccionado.")

            news_by_employee = {}
            for news in news_records:
                emp_id = news.employee_id.id
                if emp_id not in news_by_employee:
                    news_by_employee[emp_id] = {
                        'employee': news.employee_id,
                        'news': []
                    }
                news_by_employee[emp_id]['news'].append(news)

            buffer = StringIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter,
                                    rightMargin=30, leftMargin=30,
                                    topMargin=30, bottomMargin=30)
            elements = []
            styles = getSampleStyleSheet()

            logo_path = get_module_resource('odoo8_module_news_distefano', 'static', 'description', 'logo.png')
            logo = Image(logo_path)
            max_width = 6 * inch
            max_height = 1.5 * inch
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
            title_style.alignment = 1

            subtitle_style = styles['Heading2']
            subtitle_style.alignment = 1
            subtitle_style.fontSize = 14 
            subtitle_style.spaceBefore = 6

            title = Paragraph("REPORTE DE NOTICIAS INTERNAS", title_style)
            elements.append(title)

            month_name = dict(self.fields_get(allfields=['month'])['month']['selection']).get(wizard.month, wizard.month)
            subtitle = Paragraph("{} {}".format(month_name, wizard.year), subtitle_style)
            elements.append(subtitle)

            elements.append(Spacer(1, 12))


            info_style = styles['BodyText']

            for emp_data in news_by_employee.values():
                employee = emp_data['employee']

                emp_title = Paragraph("<b>{}</b>".format(employee.name), styles['Heading2'])
                elements.append(emp_title)
                elements.append(Spacer(1, 10))

                employee_info = [
                    "<b>Cargo:</b> {}".format(employee.job_id.name if employee.job_id else "N/A"),
                    "<b>Departamento:</b> {}".format(employee.department_id.name if employee.department_id else "N/A"),
                ]
                for info in employee_info:
                    elements.append(Paragraph(info, info_style))
                elements.append(Spacer(1, 10))

                data = [['Fecha Inicio', 'Fecha Fin', 'Tipo', 'Descripción']]
                for news in emp_data['news']:
                    data.append([
                        news.start_date or "",
                        news.end_date or "",
                        Paragraph(news.type_id.name or "", styles['BodyText']),
                        Paragraph(news.description or "", styles['BodyText'])
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
                'file_name': 'Noticias_Mes{}_{}.pdf'.format(wizard.month, wizard.year)
            })

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'odoo8_module_news_distefano.news_monthly_report_wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'target': 'new',
        }

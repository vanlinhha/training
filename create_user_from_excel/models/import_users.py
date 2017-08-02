# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
import xlwt, xlrd, cStringIO
from . import read_users_in_file


class ImportUsers(models.TransientModel):
    _name = 'import.users.wizard'

    data = fields.Binary('File', required=True)
    data_err = fields.Binary('File Error')
    state = fields.Selection([('choose', 'choose'), ('get', 'get'), ('successful', 'successful')], default='choose')
    filename = fields.Char('Filename', required=True)

    @api.multi
    def reload_tree_view(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'reload'
        }

    @api.multi
    def do_import(self):
        data = base64.decodestring(self.data)
        file_type = self.filename.split('.')[-1]
        rfa = read_users_in_file.GetFixedAssets()

        if file_type == "csv":
            data = data.replace('\r', '')
            lines = data.split("\n")
            list_fixed_assets = rfa.read_csv_file(lines)
        elif file_type == "xls":
            book = xlrd.open_workbook(file_contents=data, encoding_override='utf8')
            sheet1 = book.sheet_by_index(0)
            list_fixed_assets = rfa.read_xls_file(sheet1, book)
        else:
            raise UserError("Import wizard doesn't support this file type!!")

        if list_fixed_assets == 'Wrong file format':
            raise UserError("Wrong file format")
        file_error = self._import_account_invoice(list_fixed_assets)
        if file_error:
            self.write({
                'state': 'get',
                'data_err': file_error,
                'filename': 'log_error.xls',
            })
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'import.account.asset.asset.wizard',
                'view_mode': 'form',
                'view_type': 'form',
                'res_id': self.id,
                'views': [(False, 'form')],
                'target': 'new',
            }
        else:
            self.write({
                'state': 'successful',
            })
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'import.account.asset.asset.wizard',
                'view_mode': 'form',
                'view_type': 'form',
                'res_id': self.id,
                'views': [(False, 'form')],
                'target': 'new',
            }

    @api.model
    def get_id_of_view_import(self):
        return self.env.ref('create_user_from_excel.import_user_form').id

    @staticmethod
    def _export_customer_invoice_errors(errors):

        wb = xlwt.Workbook(encoding='utf8')
        sheet = wb.add_sheet('sheet')
        sheet.write(0, 0, "Customer")
        sheet.write(0, 1, "Invoice Date")
        sheet.write(0, 2, "Currency")
        sheet.write(0, 3, "Journal")
        sheet.write(0, 4, "Account (on Other Info tab)")
        sheet.write(0, 5, "Company")
        sheet.write(0, 6, "Description")
        sheet.write(0, 7, "Account (on each line of Invoice Lines tab)")
        sheet.write(0, 8, "Quantity")
        sheet.write(0, 9, "Unit Price")
        sheet.write(0, 10, "Errors")
        index = 0

        for item in errors:
            sheet.write(index + 1, 0, item.get('partner_id'))
            sheet.write(index + 1, 1, item.get('date_invoice'))
            sheet.write(index + 1, 2, item.get('currency_id'))
            sheet.write(index + 1, 3, item.get('journal_id'))
            sheet.write(index + 1, 4, item.get('account_infor_id'))
            sheet.write(index + 1, 5, item.get('company_id'))
            sheet.write(index + 1, 6, item.get('name'))
            sheet.write(index + 1, 7, item.get('account_lines_id'))
            sheet.write(index + 1, 8, item.get('quantity'))
            sheet.write(index + 1, 9, item.get('price_unit'))
            sheet.write(index + 1, 10, item.get('errors'))
            index += 1

        data_err = cStringIO.StringIO()
        wb.save(data_err)
        data_err.seek(0)
        out = base64.encodestring(data_err.read())
        data_err.close()

        return out

    def _import_customer_invoice(self, list_fixed_assets):
        list_checked_data = []
        for invoice in list_fixed_assets:
            errors = invoice.get('errors')
            # if not errors equal to value has correct format
            vals = {}
            account_lines = []
            vals_account_line = {}
            if not errors:
                errors = ''
                # check account exist
                partner = self.env['res.partner'].search(
                    [('name', '=', invoice.get('partner_id')),
                     ('customer', '=', True)], limit=1)
                if not partner:
                    errors += 'Customer does not exist --- '
                else:
                    vals.update({
                        'partner_id': partner.id
                    })

                # check currency exist
                currency = self.env['res.currency'].search([('active', '=', True),
                                                            ('name', '=', invoice.get('currency_id'))], limit=1)
                if not currency:
                    errors += 'Currency does not exist --- '
                else:
                    vals.update({
                        'currency_id': currency.id
                    })

                # check date_invoice correct format (can be empty)
                if invoice.get('date_invoice'):
                    if not self.is_date(invoice.get('date_invoice')):
                        errors += 'Date invoice is incorrect format (correct format MM-DD-YY; eg: 02-22-17) --- '
                    else:
                        vals.update({
                            'date_invoice': invoice.get('date_invoice')
                        })

                # check correct company
                company = self.env['res.company'].search([('name', '=', invoice.get('company_id'))], limit=1)
                current_company = self.env['res.company']._company_default_get('import.account.asset.asset.wizard')
                if not company:
                    errors += 'Company does not exist --- '
                elif company.id != current_company.id:
                    errors += 'Cannot create moves for different companies --- '
                else:
                    vals.update({
                        'company_id': company.id
                    })
                    # check journal exist
                    journal = self.env['account.journal'].search([('name', '=', invoice.get('journal_id')),
                                                                  ('company_id', '=', company.id),
                                                                  ('type', '=', 'sale')
                                                                  ], limit=1)
                    if not journal:
                        errors += 'Journal does not exist --- '
                    else:
                        vals.update({
                            'journal_id': journal.id
                        })

                    # check account other infor exist
                    account_other_info = self.env['account.account'].search(
                        [('name', '=', invoice.get('account_infor_id')),
                         ('company_id', '=', company.id),
                         ('internal_type', '=', 'receivable'),
                         ('deprecated', '=', False)], limit=1)
                    if not account_other_info:
                        errors += 'Account on Other Infor tab does not exist --- '
                    else:
                        vals.update({
                            'account_id': account_other_info.id
                        })

                    # check account invoice lines exist
                    account_invoice_lines = self.env['account.account'].search(
                        [('name', '=', invoice.get('account_lines_id')),
                         ('company_id', '=', company.id),
                         ('internal_type', '=', 'other')])
                    if not account_invoice_lines:
                        errors += 'Account on Invoice Lines tab does not exist --- '
                    else:
                        vals_account_line.update({
                            'account_id': account_invoice_lines.id
                        })

                if not invoice.get('name'):
                    errors += 'Name can not is empty --- '
                else:
                    vals_account_line.update({
                        'name': invoice.get('name')
                    })

                if not invoice.get('quantity'):
                    errors += 'Quantity can not is empty --- '
                elif not self.is_float_number(invoice.get('quantity')):
                    errors += 'Quantity must be a number --- '
                else:
                    vals_account_line.update({
                        'quantity': float(invoice.get('quantity'))
                    })

                if not invoice.get('price_unit'):
                    errors += 'Unit Price can not is empty --- '
                elif not self.is_float_number(invoice.get('price_unit')):
                    errors += 'Unit Price must be a number --- '
                else:
                    vals_account_line.update({
                        'price_unit': float(invoice.get('price_unit'))
                    })

                correct_format_line_ids = [0, False, vals_account_line]
                account_lines.append(correct_format_line_ids)
                vals.update({
                    'invoice_line_ids': account_lines
                })

            # if all values are ok, create record(s)
            if not errors:
                vals.update({
                    'type': 'out_invoice'
                })
                self.env['account.invoice'].create(vals)
            # else, print record has wrong value with addition column
            else:
                data_checked = {}
                data_checked.update({
                    'partner_id': invoice.get('partner_id'),
                    'date_invoice': invoice.get('date_invoice'),
                    'currency_id': invoice.get('currency_id'),
                    'journal_id': invoice.get('journal_id'),
                    'account_infor_id': invoice.get('account_infor_id'),
                    'company_id': invoice.get('company_id'),
                    'name': invoice.get('name'),
                    'account_lines_id': invoice.get('account_lines_id'),
                    'quantity': invoice.get('quantity'),
                    'price_unit': invoice.get('price_unit'),
                    'errors': errors,
                })
                list_checked_data.append(data_checked)

        if list_checked_data:
            file_error = self._export_customer_invoice_errors(list_checked_data)
            return file_error


    def _import_account_invoice(self, list_fixed_assets):
        type_account_invoice = list_fixed_assets.pop(0) if type(list_fixed_assets) is list else ''
        if type_account_invoice == 'Customer':
            return self._import_customer_invoice(list_fixed_assets)
        elif type_account_invoice == 'Vendor':
            return self._import_vendor_bill(list_fixed_assets)
        else:
            return None

    def is_float_number(self, value):
        try:
            return isinstance(float(str(value)), float)
        except ValueError:
            return False

    def is_date(self, date):
        try:
            return True
        except ValueError:
            return False

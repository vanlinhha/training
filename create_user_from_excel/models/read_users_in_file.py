import xlrd


class GetUser():
    @staticmethod
    def read_xls_file(sheet1, book):

        list_users = []
        # if first row has wrong number column --> wrong format file
        first_row = sheet1._cell_values[0]

        if len(first_row) != 10:
            return 'Wrong file format'
        for row in xrange(1, sheet1.nrows):
            user = {}
            if len(sheet1._cell_values[row]) == 10:
                user.update({
                    'username': sheet1.cell(row, 0).value,
                    'email': sheet1.cell(row, 1).value,
                    'contact_creation': sheet1.cell(row, 1).value,
                    'home_action': sheet1.cell(row, 1).value,
                    'sale': sheet1.cell(row, 1).value,
                    'project': sheet1.cell(row, 1).value,
                    'account': sheet1.cell(row, 1).value,
                    'employee': sheet1.cell(row, 1).value,
                    'timesheet': sheet1.cell(row, 1).value,
                    'administrator': sheet1.cell(row, 1).value,
                })
            else:
                user.update({
                    'errors': 'This line is wrong format;'
                })

        return list_users

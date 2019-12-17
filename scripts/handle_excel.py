"""
Time:2019/12/14 0014
"""
import openpyxl

from scripts.handle_path import EXCEL_PATH


class ExcelObj:
    pass


class HandleExcel:
    def __init__(self, sheetname, filepath=None):
        self.sheetname = sheetname
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = EXCEL_PATH

    def open_excel(self):
        self.workbook = openpyxl.load_workbook(self.filepath)
        self.sheet = self.workbook[self.sheetname]

    def read_excel(self):
        self.open_excel()
        rows_li = list(self.sheet.rows)
        head_row = [h.value for h in rows_li[0]]
        obj_li = []
        for v in rows_li[1:]:
            eo = ExcelObj()
            value_row = [vr.value for vr in v]
            vh_zip = zip(head_row, value_row)
            for vh in vh_zip:
                setattr(eo, vh[0], vh[1])
            obj_li.append(eo)
        self.workbook.close()
        return obj_li

    def write_excel(self, row_num, col_num, value):
        self.open_excel()
        self.sheet.cell(row=row_num, column=col_num, value=value)
        self.workbook.save(self.filepath)
        self.workbook.close()

if __name__ == '__main__':
    he = HandleExcel('register')
    objs = he.read_excel()
    print(objs[0].data)
import openpyxl


class Excel(object):

    def __init__(self, filename, sheet_name):
        self.filename = filename
        self.sheet_name = sheet_name

    def excel_read(self):
        workbook = openpyxl.load_workbook(filename=self.filename)
        sheet = workbook[self.sheet_name]
        # print(workbook, sheet)
        # 通过行,将表中每个单元格获取，并转成列表，便于后续提取数据
        rows = list(sheet.rows)
        # print(rows)
        # 获取用例的title
        title = []
        for i in rows[0]:
            title.append(i.value)
        # print(title)
        # 接下来获取测试用例内容

        case = []
        for i in rows[1:]:
            data = []
            for j in i:
                data.append(j.value)
            case.append(dict(zip(title, data)))
        return case


excel = Excel(r"D:\credit\data\test_case.xlsx", "login")
print(excel.excel_read())
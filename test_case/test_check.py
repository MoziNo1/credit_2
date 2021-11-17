import unittest
import unittestreport
from unittestreport import ddt, list_data
from test_case.func import TestCredit
from common.excel_handler import Excel
from common.conf_handler import conf


@ddt
class TestCheckCust(unittest.TestCase):
    excel = Excel(r"D:\credit\data\test_case.xlsx", "check")
    login_data = excel.excel_read()

    @classmethod
    def setUpClass(cls) -> None:
        cls.cookies = TestCredit().login()
        # print(cls.cookies)

    @list_data(login_data)
    def test_check(self, item):
        res = TestCredit().check_add(self.cookies, item)
        # print(self.cookies)
        print(res)
        try:
            self.assertEqual(res["description"],item["expected"])
            print(f"{item['case_id']}--{item['title']}--测试通过")
        except AttributeError as e:
            print(f"{item['case_id']}--{item['title']}--测试未通过")
            raise e


if __name__ == '__main__':
    unittest.main()
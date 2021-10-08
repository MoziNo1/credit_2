import unittest
import re
from unittestreport import ddt, list_data
from test_case.func import TestCredit
from common.excel_handler import Excel
from common.conf_handler import conf
from log.log_handler import log
from id_card.ganle import ident_generator

@ddt
class TestAddCust(unittest.TestCase):
    excel = Excel(r"D:\credit\data\test_case.xlsx", "add")
    # 新建客户的数据
    add_data = excel.excel_read()
    # 用于校验当前身份证号可否用来新建客户
    check_data = conf.get("check", "add_data")
    # 找出要替换的内容
    data = re.findall("\*.+?\*", check_data)
    check_data = check_data.replace(data[0], ident_generator())
    check_data = eval(check_data)
    print(type(check_data))

    @classmethod
    def setUpClass(cls) -> None:
        # 前置条件，需获取到登陆后的cookie
        cls.cookies = TestCredit().login(login_data=conf.get("login", "login_data"))
        res = TestCredit().check_add(cls.cookies, cls.check_data)
        # 从检验是否可新增接口中获取新增用户所用的数据，进行参数关联
        cls.replace = [res["data"]["cstNumb"], res["data"]["crdtNo"], res["data"]["cstNm"]]
        log.info(res["description"])

    @list_data(add_data)
    def test_save(self, item):
        data = item["data"]
        find = re.findall("\*.+?\*", data)
        # print(type(find))
        for i in find:
            print(find.index(i))
            data = data.replace(i, self.replace[find.index(i)])
        # print(data)
        item["data"] = data
        # print(item["data"])
        res = TestCredit().cust_personal_add(self.cookies, item)
        # print(self.cookies)
        print(res)
        try:
            self.assertEqual(res["description"], item["expected"])
            log.info(res["description"])
            print(f"{item['case_id']}--{item['title']}--测试通过")
        except AttributeError as e:
            log.error(res['description'])
            print(f"{item['case_id']}--{item['title']}--测试未通过")
            raise e


if __name__ == '__main__':
    unittest.main()
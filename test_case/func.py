import requests
import unittestreport
from common.conf_handler import conf


class TestCredit(object):

    def __init__(self):
        self.basic_url = conf.get("common", "basic_url")
        self.headers = conf.get("common", "headers")

    def login(self, login_data):
        s = requests.session()
        case_data = eval(login_data)
        login_url = self.basic_url + "/login"
        headers = eval(self.headers)
        res = s.request("post", url=login_url, data=case_data, headers=headers)
        cookies = requests.utils.dict_from_cookiejar(s.cookies)
        # print(res.text)
        print(cookies)
        return cookies

    def check_add(self, cookie, case_data):
        check_url = self.basic_url + case_data["url"]
        headers = eval(self.headers)
        check_data = eval(case_data["data"])
        # add_data = case_data["data"]
        res = requests.request("post", url=check_url, cookies=cookie, data=check_data, headers=headers)
        return res.json()

    def check_corporat_add(self, cookie, case_data):
        print(case_data)
        print(case_data['url'])
        check_url = self.basic_url + case_data["url"]
        headers = eval(self.headers)
        check_data = eval(case_data["data"])
        # add_data = case_data["data"]
        res = requests.request("post", url=check_url, cookies=cookie, data=check_data, headers=headers)
        return res.json()

    def cust_personal_add(self, cookie, case_data):
        add_url = self.basic_url + case_data["url"]
        headers = eval(self.headers)
        add_data = eval(case_data["data"])
        # add_data = case_data["data"]
        res = requests.request("post", url=add_url, cookies=cookie, data=add_data, headers=headers)
        return res.json()

    def corproat_add(self, cookie, case_data):
        add_url = self.basic_url + case_data["url"]
        headers = eval(self.headers)
        add_data = eval(case_data["data"])
        # add_data = case_data["data"]
        res = requests.request("post", url=add_url, cookies=cookie, data=add_data, headers=headers)
        return res.json()
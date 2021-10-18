import unittest
import requests

from common.conf_handler import conf

login_url = 'http://172.21.1.146:8180/xyjk-erp-app-pc/login'
headers = conf.get("common", "headers")
s = requests.session()
print(conf.get("login", "login_data"))
headers = eval(headers)
login_data = eval(conf.get("login", "login_data"))
res = s.post(url=login_url, data=login_data,headers=headers)
cookies = requests.utils.dict_from_cookiejar(s.cookies)
print(res.text)
print(cookies)
for i in range(130,150):
    add_data = {"loginName": i,
                "realname": "压测",
                "password": "a111111",
                "repassword": "a111111",
                "statusCd": "1",
                "buttonType": "saveBizInf",
                "_actionLoaction": "我的设置 > 系统管理 > 用户管理 > 用户信息",
                "_actionMuneId": "RES10003",
                "_selectTabName": "基本信息",
                "_buttonName": "保存",
                "location_url": ""}
    url1 = 'http://172.21.1.146:8180/xyjk-erp-app-pc/usermg/save'
    headers["X-Requested-With"] = 'XMLHttpRequest'
    res = requests.post(url=url1, cookies=cookies, data=add_data, headers=headers)
    user_num = res.json()["data"]["userNum"]
    print(res.text)

    url2 = 'http://172.21.1.146:8180/xyjk-erp-app-pc/usermg/userAndOrgRel/save'
    add_data2 = {
        'userNum': user_num,
        "orgCode": 1198,
        "orgName": "华兴银行总行",
        "deptCode": 119801,
        "deptName": "总行主管",
        "orgCode_field_suffixsign": "1qO3O11KLcSF",
        "all_dynamic_field": "orgCode_field_suffixsign,deptCode_field_suffixsign,roleCode_field_suffixsign,",
        "deptCode_field_suffixsign": '1O!jF00Y0k0x',
        "roleCode": "RLS0010",
        "roleName": "总行行长",
        "roleCode_field_suffixsign": "1X5ary1U5TJU",
        "statusCd": 1,
        "defaultInd": 1,
        "checkRequestSign": "",
        "realname": "压测啊",
        "_actionLoaction": "我的设置 > 系统管理 > 用户管理 > 用户信息",
        "_actionMuneId": "RES10003",
        "_selectTabName": "角色",
        "_buttonName": "提交",
        "location_url": ""}
    res2 = requests.post(url=url2, cookies=cookies, data=add_data2, headers=headers)
    print(res2.text)

    url3 = 'http://172.21.1.146:8180/xyjk-erp-app-pc/usermg/userAndDeptRel/save'
    add_data3 = {
        "userNum": user_num,
        "orgCode": "1198",
        "orgName": "华兴银行总行",
        "deptCode": "119801",
        "deptName": "总行主管",
        "statusCd": 1,
        "checkRequestSign": "",
        "_actionLoaction": "我的设置 > 系统管理 > 用户管理 > 用户信息",
        "_actionMuneId": "RES10003",
        "_selectTabName": "所属部门",
        "_buttonName": "提交",
        "location_url": ""
    }

    res3 = requests.post(url=url3, cookies=cookies, data=add_data3, headers=headers)
    print(res3.text)

    url4 = 'http://172.21.1.146:8180/xyjk-erp-app-pc/usermg/userAndRoleRel/save'
    add_data4 = {
        "userNum": user_num,
        "orgCode": '1198',
        "orgName": '华兴银行总行',
        "deptCode": '119801',
        "deptName": '总行主管',
        "orgCode_field_suffixsign": '1qO3O11KLcSF',
        "all_dynamic_field": 'orgCode_field_suffixsign,deptCode_field_suffixsign,roleCode_field_suffixsign,',
        "deptCode_field_suffixsign": '1O!jF00Y0k0x',
        "roleCode": 'RLS0010',
        "roleName": '总行行长',
        "roleCode_field_suffixsign": '1X5ary1U5TJU',
        "statusCd": 1,
        "defaultInd": 1,
        "checkRequestSign": '',
        "realname": '压测啊',
        "_actionLoaction": '我的设置 > 系统管理 > 用户管理 > 用户信息',
        "_actionMuneId": 'RES10003',
        "_selectTabName": '角色',
        "_buttonName": '	提交',
        "location_url": ''
    }

    res4 = requests.post(url=url4, cookies=cookies, data=add_data4, headers=headers)
    print(res4.text)
    # #



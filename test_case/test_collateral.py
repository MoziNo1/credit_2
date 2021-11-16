import requests
from test_case.func import TestCredit
from common.conf_handler import conf
from common.database_handler import mysql

login_url = 'http://172.21.1.146:8180/xyjk-erp-app-pc/login'
collateral_url = 'http://172.21.1.146:8180/xyjk-erp-app-pc/cltRgs/save'
login_data = eval(conf.get('login', 'login_data'))
tenant_search_sql = f"select c.tenant_id from sys_user c where c.login_name = '{login_data['username']}'"
mysql.mysql_do(tenant_search_sql)
tenant_id = mysql.mysql_do(tenant_search_sql)[0][0]
print(tenant_id)
cust_no = input("请输入您的证件号:")
if len(cust_no) == len('451709195904018434'):
    cust_search_sql = f"select c.Cust_Nm, c.Cust_Numb, c.cbs_cus_no from cust_personal c where c.Ctf_Nbr ='{cust_no}' and c.tenant_id = '{tenant_id}' "
else:
    cust_search_sql = f"select c.Chn_Nm,c.Cust_Numb, c.cbs_cus_no from cust_corporat c where c.Org_Inst_Code = '{cust_no} and c.tenant_id = '{tenant_id}' "
cust_data = mysql.mysql_do(cust_search_sql)
# print(cust_data[0][0],cust_data[0][1],cust_data[0][2])
s = requests.session()
headers = eval(conf.get("common", "headers"))
case_data = {
    "eqmtNm": "设备名",
    "pmss": "长春市",
    "cstNumb": cust_data[0][1],
    "cltTp": "05",
    "cltCgy": "01",
    "tpId": "",
    "cltNm": "抵押物",
    "cltAdr": "吉林省长春市",
    "cityCode": "",
    "rmrk": "",
    "cstNm": cust_data[0][0],
    "wrntNumb": "12345",
    "useWghtPsn": cust_data[0][2],
    "bnkNm": "",
    "alctAmt": "",
    "iouAmt": "",
    "loanStarDt": "",
    "wrntPnamt": "60000",
    "asesAmt": "60000",
    "cltPlgRate": "100.0000",
    "_actionLoaction": "押品管理 > 押品管理 > 押品登记",
    "_actionMuneId": "RES10783",
    "_selectTabName": "",
    "_buttonName": "保存",
    "location_url": "",
}
res = s.request("post", url=login_url, data=login_data, headers=headers)
cookies = requests.utils.dict_from_cookiejar(s.cookies)
# print(cookies)
collateral_response = s.request("post", url=collateral_url, data=case_data, headers=headers)
print(collateral_response.text)

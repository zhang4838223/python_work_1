import requests
import json
import sys

input_param = sys.argv[1]+sys.argv[2]+sys.argv[3]+sys.argv[4]+sys.argv[5]+sys.argv[6]+sys.argv[7] + sys.argv[8] + sys.argv[9]
# input_param = gr_user_id=ab9ffcc6-26be-45ca-9ef3-fffbc9e8836f; sessionid=0x8k3815mzca0qdlr6yuyprpjxtzbnkn; Hm_lvt_2897b5c5139f101b1546330e08d6d3ea=1576804163,1577063162,1577173890,1577322189; null#day_ana=10; null#isToday=Y; zg_sso_token=M5orrHJCEQfmd9RB8B75WXHlkkOsq0QTEtCeOY6msdi3YefY1hcijbLWDOHf_qe5a-HfttSJ5Rp3ReOWH7-k_A..; portalCookie=EgN_9fwUf1X11yRPZlWuR2Np0cebMW-gQSzeCRM5JnUd38u_xdeEyZSZ03A2U1HJsX3Sr--bQk4.; Hm_lpvt_2897b5c5139f101b1546330e08d6d3ea=1577329026; favor_system_alias=finance.basedata.platform.api
input_arr = input_param.split(";")
cookie_param = {}
print("input_param" + "===>" + input_param)
for input in input_arr:
    key_value = input.split("=")
    cookie_param[key_value[0]] = key_value[1]

print("cookie_param" + "===>" + str(input_param))

systemArr = ['purchase.baseinfo.globalstock.api', 'purchase.baseinfo.globalstock.ui','purchase.purchasemanagement.selfmanagement.api',
             'purchase.purchasemanagement.selfmanagement.ui', 'inventory.scm.management.api','inventory.scm.management.ui',
             'inventory.scm.onsale.api','inventory.scm.onsale.ui', 'finance.basedata.platform.api','basicplatform.saas.report.service']

for sysName in systemArr[0:]:
    print("===========" + sysName + "===========")
    param = {
        "product":sysName,
        "runEnv":"40",
        "logLevel":"3",
        "starttime":"2019-12-26 00:00:00",
        "endtime":"2019-12-26 23:59:59",
        "topicBySdk":"false",
        "page":"1",
        "rows":"20",
        "order":"desc"
    }

    result = requests.post(
    "http://log.arch.zhaogangren.com/query/getApplogData/",
        data = param,
        cookies=cookie_param
    )

    jsonResult = json.loads(result.text)
    rows = jsonResult["rows"]
    total = jsonResult["total"]
    if (total > 0) :
        for item in rows[0:]:
            content = item['content']
            print(sysName + "              " + content)

    print("【" + sysName + "】 error log num:" + str(total))

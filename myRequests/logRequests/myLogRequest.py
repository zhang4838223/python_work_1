import requests
import json
import itchat

cookies = dict(gr_user_id='ab9ffcc6-26be-45ca-9ef3-fffbc9e8836f',
               sessionid="f578vcg52256w5jeygtqd29t9de7nfpk",
               zg_sso_token="M5orrHJCEQfmd9RB8B75WXHlkkOsq0QTEtCeOY6msdi3YefY1hcijTy2z-JWi_kiy7Q4HsKYkrkMVKQfv7R94Q..",
portalCookie="EgN_9fwUf1X11yRPZlWuR2Np0cebMW-gQSzeCRM5JnUd38u_xdeEyZSZ03A2U1HJsX3Sr--bQk4.",
Hm_lvt_2897b5c5139f101b1546330e08d6d3ea="1561770362,1561943263,1562029530,1562118217",
Hm_lpvt_2897b5c5139f101b1546330e08d6d3ea="1562118217",
favor_system_alias="purchase.baseinfo.globalstock.api"

               )
result = requests.post(
"http://log.arch.zhaogangren.com/query/getApplogData/",
    data = {
        "product":"purchase.baseinfo.globalstock.api",
        "runEnv":"40",
        "logLevel":"3",
        "starttime":"2019-07-03 00:00:00",
        "endtime":"2019-07-03 23:59:59",
        "topicBySdk":"false",
        "page":"1",
        "rows":"20",
        "order":"desc"
                      },
    cookies=cookies
)

jsonResult = json.loads(result.text)
print(jsonResult["total"])

if jsonResult["total"] > 0 :
    notifyUrl = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=719142e4-f684-469c-8299-731a20a75716"
    notifData = {
    "msgtype": "text",
    "text": {
        "content": "error日志数量" + str(jsonResult["total"]),
        "mentioned_list":["@all"]
        }
    }
## print(notifData)
##  result = requests.post(notifyUrl, notifData)
else:
    print("no error!!")


def after_login():
    # 获取群聊列表
    room = itchat.search_chatrooms(name="全村的希望")
    print(len(room))
    allRooms=itchat.get_chatrooms()
    print("all" + str(len(allRooms)))
    if len(room) > 0:
        itchat.send_msg("error日志数量" + str(jsonResult["total"]), room[0]["UserName"])

if __name__ == '__main__':
    itchat.auto_login(loginCallback=after_login, hotReload=True)
    itchat.run

import os
import requests
import json
from datetime import datetime

url = "https://hweb-mbf.huazhu.com/api/signIn"

headers = {
    "Host": "hweb-mbf.huazhu.com",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, brgzip, deflate, br",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://campaign.huazhu.com",
    "User-Agent": "HUAZHU/ios/iPhone14,3/16.3.1/9.9.0/HUAZHU/ios/iPhone14,3/16.3.1/9.9.0/Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Client-Platform": "APP-IOS",
    "Referer": "https://campaign.huazhu.com/",
    "User-Token": "null",
    "Content-Length": "14",
    "Cookie": os.environ['MY_COOKIE'],
    "Connection": "keep-alive"
}

curren_day = datetime.now().day
data = f"state=1&day={curren_day}"

response = requests.post(url, headers=headers, data=data)

# 使用 Server 酱发送消息
sckey = os.environ['SCKEY']
server_url = f"https://sc.ftqq.com/{sckey}.send"

if response.status_code == 200:
    message_title = f"OK, day: {data}"
    message = f"ok,status code: {response.status_code}, response text: {response.text}"
else:
    message_title = f"Sorry, day: {data}"
    message = f"no, status code: {response.status_code}, response text: {response.text}"

server_data = {
    "text": message_title,
    "desp": message
}


requests.post(server_url, data=server_data)

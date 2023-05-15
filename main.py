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
    "Cookie": "SK=79cd4f7c63864016b087c95f473b1191302369329; _efmdata=GFcYLK0HhSE7AwVCo%2BfMIeF3PS16Sf089nCTZr27LYSKklcxVHZ4kEqFrydggNqTb00EzOQWgk6McXS8jMX6Jz0zSPALEmkayyzMRuDRgHc%3D; _exid=8d2bwkq5qPlMWnp8qkBDeRTFciW8UGgklBqUZWe0tYlknnu5GRJFf09hq7vKqTU0pnCWdY7w%2F5RKlk%2B5qSuuEA%3D%3D; _hudPVID=45; _hudSID=1683908059185_6; _hudSID_TS=1683908059185; _hudSource=; ec=4hsiYY49-1683849531264-a880e1fa29e721487644933; userToken=79cd4f7c63864016b087c95f473b1191302369329; CSRF-NWACT=853fbf60-9050-4cd5-8e6d-81ea3c78b458; _ga=GA1.2.794502254.1683887912; gr_session_id_8f6e3e7f89d647cab9784afa81ea87bd=edff68ae-c8aa-4f9e-90aa-69e3eaa202cc; gr_session_id_8f6e3e7f89d647cab9784afa81ea87bd_edff68ae-c8aa-4f9e-90aa-69e3eaa202cc=false; gr_user_id=e07a25e2-cd50-4cca-bec4-184e0d019a74; install_id=7014107406015694604; ttreq=1$b93d3c873c3b0e79dac3322f4f3c7bd462abd732; _fmdata=CYLWmtJBeDowLqZtV%2BC7gIxgJgma0bzG7OTq26NVnQcLgE1KxpL7m0f2xVLD2yNxOQCZ88%2Fqy8fK%2BdhkhJNa3w%3D%3D; _xid=opPtk5kCBVGdxSYL1pDOVS%2FQQ%2FyeRjx1spyLPBkUkJc%3D; c=4hsiYY49-1683849531264-a880e1fa29e721487644933; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2240149125%22%2C%22first_id%22%3A%221880f2f48d3595-02da2d1d01a7cf8-6d10304d-396328-1880f2f48d4be8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221880f2f48d3595-02da2d1d01a7cf8-6d10304d-396328-1880f2f48d4be8%22%7D; _hudVID=3bebb8c6-b1d0-4658-539a-fb07cafcd8f8",
    "Connection": "keep-alive"
}

curren_day = datetime.now().day
data = f"state=1&day={curren_day}"

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    print("ok")
else:
    print("no")
    print(response.status_code, response.text)

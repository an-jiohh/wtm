import requests
import json

with open("kakao_code.json", "r") as fp:
    tokens = json.load(fp)    

print(tokens["access_token"])

url = "https://kapi.kakao.com/v1/api/talk/friends" #친구 목록 가져오기
header = {"Authorization": 'Bearer ' + tokens["access_token"]}

result = json.loads(requests.get(url, headers=header).text)
friends_list = result.get("elements")

print(friends_list)

friend_id = friends_list[0].get("uuid")
print(friend_id)

url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
header = {"Authorization": 'Bearer ' + tokens["access_token"]}

data={
    'receiver_uuids': '["{}"]'.format(friend_id),
    "template_object": json.dumps({
        "object_type":"text",
        "text": "흑미밥, 열무국, 돈갈비떡찜, 미트볼조림, 미역오이초무침, 초코우유, 배추김치",
        "link":{
            "web_url" : "https://www.google.co.kr/search?q=deep+learning&source=lnms&tbm=nws",
            "mobile_web_url" : "https://www.google.co.kr/search?q=deep+learning&source=lnms&tbm=nws"
        },
        "button_title": "뉴스 보기"
    })
}

response = requests.post(url, headers=header, data=data)
response.status_code
import requests
import json

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers = {
    "Authorization": "Bearer " + ""
}

template = {
    "object_type" : "list",
    "header_title" : "Google",
    "header_link" : {
        "web_url" : "www.google.com",
        "mobile_web_url" : "www.google.com"
    },
    "contents" : [
        {
            "title" : "1. 국립공원 뉴스",
            "description" : "검색어: national park",
            "image_url" : "https://cdn.kado.net/news/photo/201901/948844_399953_0825.jpg",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "https://www.google.co.kr/search?q=national+park&source=lnms&tbm=nws",
                "mobile_web_url" : "https://www.google.co.kr/search?q=national+park&source=lnms&tbm=nws"
            }
        },
        {
            "title" : "2. 딥러닝 뉴스",
            "description" : "검색어: deep learning",
            "image_url" : "https://cdn-images-1.medium.com/max/1200/1*iDQvKoz7gGHc6YXqvqWWZQ.png",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "https://www.google.co.kr/search?q=deep+learning&source=lnms&tbm=nws",
                "mobile_web_url" : "https://www.google.co.kr/search?q=deep+learning&source=lnms&tbm=nws"
            }
        }
        
    ],
    "buttons" : [
        {
            "title" : "Google로 이동",
            "link" : {
                "web_url" : "www.google.com",
                "mobile_web_url" : "www.google.com"
            }
        }
    ]
    
}

data = {
    "template_object" : json.dumps(template)
}

response = requests.post(url, data=data, headers=headers)
# print(response.status_code)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
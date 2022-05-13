from get_friends_list import get_list
import requests
import json

def send_ksnu_menu(menu) :

    with open("kakao_code.json", "r") as fp:
        tokens = json.load(fp)    

    friends_list = get_list(tokens["access_token"]) #친구 목록을 가져오는 함수

    print(friends_list)
    
    friends_id = [] #친구목록에서 id만 가져옴
    for i in friends_list :
        friends_id.append(i.get("uuid"))

    url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
    header = {"Authorization": 'Bearer ' + tokens["access_token"]}

    data={
        'receiver_uuids': json.dumps(friends_id[0:1]),
        "template_object": json.dumps({
            "object_type":"text",
            "text": "{}".format(menu),
            "link":{
                "web_url" : "https://www.kunsan.ac.kr/dormi/index.kunsan?menuCd=DOM_000000704006003000",
                "mobile_web_url" : "https://www.kunsan.ac.kr/dormi/index.kunsan?menuCd=DOM_000000704006003000"
            }
        })
    }

    response = requests.post(url, headers=header, data=data)
    print(response.status_code)
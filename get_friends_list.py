import json
import requests

def get_list(token):
    url = "https://kapi.kakao.com/v1/api/talk/friends" #친구 목록 가져오기
    header = {"Authorization": 'Bearer ' + token}

    result = json.loads(requests.get(url, headers=header).text)
    friends_list = result.get("elements")
    fridens_num = result.get("total_count")

    print(fridens_num)
    return friends_list

with open("kakao_code.json", "r") as fp:
    tokens = json.load(fp)    

test_list = get_list(tokens["access_token"])
print(test_list)
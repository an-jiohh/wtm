import requests
import json

def refresh_token() :
    url = "https://kauth.kakao.com/oauth/token"

    data = {
        "grant_type": "refresh_token",
        "client_id": "",
        "refresh_token": ""
    }
    response = requests.post(url, data=data)
    tokens = response.json()

    # kakao_code.json 파일 저장
    with open("kakao_code.json", "w") as fp:
        json.dump(tokens, fp)

 # refresh_token() #액세스 토큰재발급 필요할때 실행
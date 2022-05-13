import requests
import json

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "",
    "redirect_url" : "https://localhost:3000",
    "code" : ""
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)
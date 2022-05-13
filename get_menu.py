import requests
from bs4 import BeautifulSoup

def get_ksnu_menu() :
    URL = f"https://www.kunsan.ac.kr/dormi/index.kunsan?menuCd=DOM_000000704006003000"

    html = requests.get(URL)

    soup = BeautifulSoup(html.text, "html.parser")
    tables = soup.find_all("table",{"class":"ctable01"})
    table = tables[1]
    #tbody = table.find("tbody") //thead에 td태그가 존재하지 않아 바로 td태그로 추출하였다.
    td = table.find_all("td")

    breakfasts = td[0:7]
    lunchs = td[7:14]
    dinners = td[14:21]

    breakfast = []
    lunch = []
    dinner = []

    for i in breakfasts :
        breakfast.append(i.get_text().split())
    for i in lunchs :
        lunch.append(i.get_text().split())
    for i in dinners :
        dinner.append(i.get_text().split())

    return breakfast, lunch, dinner
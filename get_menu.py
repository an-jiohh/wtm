import requests
from bs4 import BeautifulSoup

URL = f"https://www.kunsan.ac.kr/dormi/index.kunsan?menuCd=DOM_000000704006003000"

html = requests.get(URL)

soup = BeautifulSoup(html.text, "html.parser")
tables = soup.find_all("table",{"class":"ctable01"})
table = tables[1]
asdf = table.find("tbody")
zxcvs = asdf.find_all("td")

breakfasts = zxcvs[0:7]
lunchs = zxcvs[7:14]
dinners = zxcvs[14:21]

breakfast = []
lunch = []
dinner = []

for i in breakfasts :
    breakfast.append(i.get_text().split())
for i in lunchs :
    lunch.append(i.get_text().split())
for i in dinners :
    dinner.append(i.get_text().split())

print(breakfast)
print(lunch)
print(dinner)
from get_menu import get_ksnu_menu
from send_menu import send_ksnu_menu
from get_access_token import refresh_token
import time

now = time
'''
!!!중요!!!
깃허브 올리기전 3요소 체크
1. get_access_token의 client_id, refresh_token 요소 삭제
2. get_refresh_token의 client_id, code 요소 삭제
3. kakao_code.json, jwt파일 삭제
체크 후 올릴 것!
'''
## 7:30 아침
## 11:30 점심
## 17:30 저녁
t = ['월','화','수','목','금','토','일']


def sel_menu(time_sel) : # time_sel(0:아침,1:점심,2:저녁)
    twd = ['월','화','수','목','금','토','일']
    t = ['아침','점심','저녁']
    breakfast, lunch, dinner = get_ksnu_menu()
    
    if time_sel == 0 : meal = breakfast[now.localtime().tm_wday]
    elif time_sel == 1 : meal = lunch[now.localtime().tm_wday]
    elif time_sel == 2 : meal = dinner[now.localtime().tm_wday]

    me = ""
    me = me + "{}월 {}일 {}요일 {}\n".format(now.localtime().tm_mon,now.localtime().tm_mday,twd[now.localtime().tm_wday],t[time_sel])
    for i in meal :
        me = me + str(i) + "\n"
    return me

while True :
    h = now.localtime().tm_hour
    m = now.localtime().tm_min
    wd = now.localtime().tm_wday
    
    print("{}:{}:{} {} ".format(h,m, now.localtime().tm_sec,t[wd]))
    if h == 7 : 
        if m == 30 :
            if wd != 5 and wd != 6 : # 토,일요일은 밥이 없음
                breakfast, lunch, dinner = get_ksnu_menu()
                me = sel_menu(0)
                send_ksnu_menu(me)
            time.sleep(60)
    if h == 11 :
        if m == 30 :
            breakfast, lunch, dinner = get_ksnu_menu()
            me = sel_menu(1)
            send_ksnu_menu(me)
            time.sleep(60)
    if h == 17 :
        if m == 30 :
            breakfast, lunch, dinner = get_ksnu_menu()
            me = sel_menu(2)
            send_ksnu_menu(me)
            time.sleep(60)
    if h== 0 :
        if m == 0 :
            print("토큰 초기화")
            refresh_token()
            time.sleep(60)
    time.sleep(30)
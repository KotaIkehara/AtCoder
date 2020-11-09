import sys
import datetime


def calcSum(userX, userY, restX, restY, money):
    dist = ((userX - restX)**2 + (userY - restY)**2)**0.5
    if(0 <= dist < 100):
        shipping = 300
    elif(100 <= dist < 1000):
        shipping = 600
    elif(1000 <= dist < 10000):
        shipping = 900
    elif(10000 <= dist):
        shipping = 1200
    return money + shipping


n, m = map(int, input().split())
holiday = [input() for i in range(n)]
restInfo = [input().split() for i in range(m)]
freeShipping = []
minMoney = []
closeDay = []
weekList = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
# EOFまでクエリを受け取る
try:
    while True:
        query = list(input().split())
        # 注文クエリの処理
        if(query[2] == "order"):
            date = query[0]
            y, m, d = map(int, date.split("-"))
            time = query[1]
            money = int(query[4])
            userX = int(query[5])
            userY = int(query[6])

            # （注文のレストランID）=（レストラン情報のレストランID）となるレストラン情報の取得
            for i in range(m):
                if(query[3] == restInfo[i][0]):
                    restX = int(restInfo[i][1])
                    restY = int(restInfo[i][2])
                    break

            # 最低注文条件を満たしていないとき
            for l in minMoney:
                if(query[3] == l[0] and money < int(l[1])):
                    print(date, time, "ERROR INSUFFICIENT")
                    break
            else:
                # 定休日の時
                for l in closeDay:
                    if(query[3] == l[0] and (weekList[datetime.date(y, m, d).weekday()] == l[1] or (date[5:] in holiday and l[1] == "HOLIDAY"))):
                        print(date, time, "ERROR CLOSED DAY")
                        break
                else:
                    # 送料無料の時
                    for f in freeShipping:
                        if(query[3] == f[0] and money >= int(f[1])):
                            print(date, time, money)
                            break
                    # 送料無料でないとき
                    else:
                        sum = calcSum(userX, userY, restX, restY, money)
                        print(date, time, sum)
        # 送料無料条件の設定
        if(query[2] == "set_free"):
            freeShipping.append(query[3:])
        # 最低注文条件の設定
        if(query[2] == "set_min"):
            minMoney.append(query[3:])
        # 定休日の設定
        if(query[2] == "close_day" and query[3:] not in closeDay):
            closeDay.append(query[3:])
        # 定休日の解除
        if(query[2] == "open_day" and query[3:] in closeDay):
            closeDay.remove(query[3:])
except EOFError:
    pass

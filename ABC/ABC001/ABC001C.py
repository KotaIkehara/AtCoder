from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

Deg, Dis = map(int, input().split())
Deg /= 112.5
if(1<= Deg < 3):
    Dir = "NNE"
elif(3 <= Deg < 5):
    Dir = "NE"
elif(5 <= Deg < 7):
    Dir = "ENE"
elif(7 <= Deg < 9):
    Dir = "E"
elif(9 <= Deg < 11):
    Dir = "ESE"
elif(11 <= Deg < 13):
    Dir = "SE"
elif(13 <= Deg < 15):
    Dir = "SSE"
elif(15 <= Deg < 17):
    Dir = "S"
elif(17 <= Deg < 19):
    Dir = "SSW"
elif(19 <= Deg < 21):
    Dir = "SW"
elif(21 <= Deg < 23):
    Dir = "WSW"
elif(23 <= Deg < 25):
    Dir = "W"
elif(25 <= Deg < 27):
    Dir = "WNW"
elif(27 <= Deg < 29):
    Dir = "NW"
elif(29 <= Deg < 31):
    Dir = "NNW"
else:
    Dir = "N"
Dis = float(Decimal(str(Dis/60)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
if(0.0 <= Dis <= 0.2):
    W = 0
elif(0.3 <= Dis <= 1.5):
    W = 1
elif(01.6 <= Dis <= 3.3):
    W = 2
elif(3.4 <= Dis <= 5.4):
    W = 3
elif(5.5 <= Dis <= 7.9):
    W = 4
elif(8.0 <= Dis <= 10.7):
    W = 5
elif(10.8 <= Dis <= 13.8):
    W = 6
elif(13.9 <= Dis <= 17.1):
    W = 7
elif(17.2 <= Dis <= 20.7):
    W = 8
elif(20.8 <= Dis <= 24.4):
    W = 9
elif(24.5 <= Dis <= 28.4):
    W = 10
elif(28.5 <= Dis <= 32.6):
    W = 11
elif(32.7 <= Dis):
    W = 12

if(W == 0):
    print("C", W)
else:
    print(Dir, W)
m = int(input())

if(m < 100):
    print("%02d" % 0)
elif(100 <= m <= 5000):
    print("%02d" % int(m*0.01))
elif(6000 <= m <= 30000):
    print("%02d" % int(m*0.001 + 50))
elif(35000 <= m <= 70000):
    print("%02d" % int(((m*0.001 - 30)/5) + 80))
elif(70000 < m):
    print("89")

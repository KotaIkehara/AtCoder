# 思いつかなかった
n = int(input())
for i in range(10000):
    a = i * 100
    b = i * 105
    if a <= n <= b:
        print(1)
        exit()
print(0)

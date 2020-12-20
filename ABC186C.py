N = int(input())

seven = set()
# 10進で7を含む数
for i in range(N+1):
    if("7" in str(i)):
        seven.add(i)

        
# 8進で7を含む
for i in range(N+1):
    num = i
    while(num>0):
        if num%8 == 7:
            seven.add(i) 
        num = num//8

print(N-len(seven))
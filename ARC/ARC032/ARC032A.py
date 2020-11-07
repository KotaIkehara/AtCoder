n = int(input())

S = sum(i for i in range(n+1))
if(S == 1):
    print("BOWWOW")
    exit()
print("WANWAN" if(all([S % i for i in range(2, int(S**0.5)+1)])) else "BOWWOW")

N = int(input())

flag1 = all(N % i for i in range(2, int(N**0.5)+1))
flag2 = str(N)[-1] != "5" and int(str(N)[-1]
                                  ) % 2 != 0 and sum(list(map(int, str(N)))) % 3 != 0
if(N == 1):
    print("Not Prime")
    exit()
print("Prime" if(flag1)
      or (flag2) else "Not Prime")

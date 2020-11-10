N = int(input())
NG = list(int(input()) for i in range(3))

if(N in NG):
    print("NO")
    exit()
for i in range(100):
    N -= 3  # Nを0に近づける最善の手は3を選ぶこと
    if(N in NG):  # 3ダメなら2を選ぶ（以下略）
        N += 1
        if(N in NG):
            N += 1
            if(N in NG):
                print("NO")
                exit()
print("YES" if(N <= 0) else "NO")

import math
N = math.factorial(int(input()))

res = 1
p = 2  # チェックする因数

# p=sqrt(N)を満たす因数を調査すれば十分
while p*p <= N:
    i = 1
    # p^k(k=1~)の倍数の個数を数えて足し合わせていく
    while(N % p == 0):
        i += 1
        N //= p

    # N!の約数の個数は i_0*i_1*...*i_k
    res *= i
    p += 1

if(N != 1):
    res *= 2
print(res % (10**9+7))

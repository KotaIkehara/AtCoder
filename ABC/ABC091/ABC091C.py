N = int(input())
R = sorted([list(map(int, input().split())) for i in range(N)], key=lambda x: x[1])[::-1]
B = sorted([list(map(int, input().split())) for i in range(N)])

res = 0
for blue in B:
    c, d = blue
    for red in R:
        a,b = red
        if(a<c and b<d):
            res += 1
            R.remove([a,b])
            break
            
print(res)
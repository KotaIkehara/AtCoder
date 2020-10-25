N = int(input())
S = input()
res = S.count("E")
cnt = res
for s in S:
    if(s == "E"):
        cnt -= 1
    else:
        cnt += 1
    res = min(res, cnt)
print(res)

sx,sy,tx,ty = map(int,input().split())

res = ""
# 1週目
res += "U"*(ty-sy)
res += "R"*(tx-sx)
res += "D"*(ty-sy)
res += "L"*(tx-sx)

# 2週目
res += "L"
res += "U"*(ty-sy+1)
res += "R"*(tx-sx+1)
res += "D"
res += "R"
res += "D"*(ty-sy+1)
res += "L"*(tx-sx+1)
res += "U"

print(res)

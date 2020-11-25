N = int(input())

res = ""
while(N):
    code = (N-1) % 26
    res = chr(code + ord("a"))+res
    N = (N-1)//26
print(res)

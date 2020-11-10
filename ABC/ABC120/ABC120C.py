S = input()
stack = []
res = 0

for s in S:
    if(not stack):
        stack.append(s)
    elif(stack[-1] != s):
        stack.pop()
        res += 2
    else:
        stack.append(s)
print(res)

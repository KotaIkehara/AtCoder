X = int(input())

res = 1

for i in range(2, X):
    for j in range(2, X):
        if(i**j <= X):
            res = max(res, i**j)
        else:
            break
print(res)

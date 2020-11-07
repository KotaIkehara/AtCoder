s = input()
k = int(input())

keys = []
for i in range(len(s)-k+1):
    keys.append(s[i:i+k])

print(len(set(keys)))

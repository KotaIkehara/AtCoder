N = int(input())
W = input()[:-1].split()
count = 0
for w in W:
    if(w.lower() == 'takahashikun'):
        count += 1
print(count)

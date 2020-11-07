import itertools

N = int(input())
L = list(map(int, input().split()))

count = 0
for list in itertools.combinations(L, 3):
    if(len(set(list)) == 3 and max(list) < (sum(list) - max(list))):
        count += 1
print(count)

from collections import Counter

N = int(input())
S = Counter([input() for i in range(N)])
print(S.most_common()[0][0])

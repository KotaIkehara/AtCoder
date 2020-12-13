import itertools
import math 
N,M = map(int,(input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

x = abs(N-M)
y = min(N,M)
for v in itertools.combinations(range(max(N,M)), x):
    for i in range()    
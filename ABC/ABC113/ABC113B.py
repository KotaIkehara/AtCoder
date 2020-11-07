N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

z = [abs(T-h*0.006-A) for h in H]
print(z.index(min(z))+1)

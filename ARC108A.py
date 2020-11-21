S, P = map(int, input().split())

x1 = (S+(S**2-4*P)**.5)/2
x2 = (S-(S**2-4*P)**.5)/2
print("Yes" if((x1 > 0 and x2 > 0) and x1.is_integer() and x2.is_integer()) else "No")

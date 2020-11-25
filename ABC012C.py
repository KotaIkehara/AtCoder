N = int(input())
R = 2025 - N

for i in range(1, 10):
    for j in range(1, 10):
        if(i*j == R):
            print(i, "x", j)

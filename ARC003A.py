N = int(input())
R = input()

GPA = 0
Trans = ["F", "D", "C", "B", "A"]
for r in R:
    GPA += Trans.index(r)
print(GPA/N)

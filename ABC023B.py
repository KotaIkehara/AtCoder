import re

N = int(input())
S = input()

print(N//2 if(re.match(r"^((abcabc)*abc|(bcabca)*b|(cabcab)*cabca)$", S)) else -1)

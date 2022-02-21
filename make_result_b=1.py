import pyperclip

ICCG = ""
SCICCG = []
DICCG = []

f = open("result.txt", "r")
line = f.readline()

while line:
    words = line.split(" ")
    if words[0] == "ICCG":
        ICCG = line[5:].replace('\n', '')
    if words[0] == "SCICCG":
        SCICCG.append(line[7:].replace('\n', ''))
    if words[0] == "DICCG":
        DICCG.append(line[6:].replace('\n', ''))
    line = f.readline()

res = ""
print(ICCG)
res += ICCG + '\n'

for i in range(9):
    if(len(SCICCG) > i):
        print(SCICCG[i])
        res += SCICCG[i]
    else:
        print("0 - -")
        res += "0 - -"
    res += '\n'

for i in range(9):
    if(len(DICCG) > i):
        print(DICCG[i])
        res += DICCG[i]
    else:
        print("0 - -")
        res += "0 - -"
    if i != 8:
        res += '\n'

pyperclip.copy(res)

import pyperclip

result = []

f = open("result.txt", "r")
line = f.readline()

while line:
    words = line.split(" ")
    if words[0] == "Ave.":
        result.append(line[12:].replace('\n', ''))
    line = f.readline()

res = ""
for i in range(9):
    if(len(result) > i):
        print(result[i])
        res += result[i]
    else:
        print("0 - -")
        res += "0 - -"
    if i != 8:
        res += '\n'

pyperclip.copy(res)

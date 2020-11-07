N = input()
H = ["2", "4", "5", "7", "9"]
P = ["0", "1", "6", "8"]
B = ["3"]

if(N[-1] in B):
    print("bon")
elif(N[-1] in P):
    print("pon")
else:
    print("hon")

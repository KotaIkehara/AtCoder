from sys import stdin
from collections import defaultdict

def read_step1(s):
    l = s.split()
    return l[0], int(l[1]), int(l[2]), int(l[3])

def read_menu(M):
    # Menu = {料理番号1:[在庫数, 価格], 料理番号2:[在庫数, 価格], ..., 料理番号M:[在庫数, 価格]}
    Menu = defaultdict(int)
    for i in range(M):
        # 料理番号，初期在庫数，価格
        D,S,P = map(int, input().split())
        Menu[D] = [S,P]
    return Menu

def step1():
    M = int(input())
    Menu = read_menu(M)

    for line in stdin:
        order, T, D, N = read_step1(line)
        stock, price = Menu[D]
        if(stock < N):
            print("sold out", T)
        else:
            for i in range(N):
                print("received order", T, D)
            Menu[D][0] -= N

def step2():
    M, K = map(int, input().split())
    Menu = read_menu(M)
   
    cooking = []
    waiting = []

    for line in stdin:
        l = line.split()
        instruction = l[0]
        if(instruction  == "complete"):
            D = int(l[1])
        elif(instruction  == "received"):
            T, D = int(l[2]), int(l[3])
        elif(instruction  == "sold"):
            continue

        if(instruction == "received" and  len(cooking) < K):
            print(D)
            cooking.append(D)
        elif(instruction == "received" and  len(cooking) == K):
            print("wait")
            waiting.append(D)
        elif(instruction == "complete" and D in cooking and len(waiting) > 0):
            print("ok", waiting[0])
            cooking.remove(D)
            cooking.append(waiting[0])
            waiting.pop(0)
        elif(instruction == "complete" and D in cooking and len(waiting) == 0):
            print("ok")
            cooking.remove(D)
        else:
            print("unexpected input")

# 完成した料理をスタッフが運べるようにする
def step3():
    M = int(input())
    Menu = read_menu(M)

    waiting = []
    for line in stdin:
        l = line.split()
        instruction = l[0]
        if(instruction  == "complete"):
            D = int(l[1])
        if(instruction == "received"):
            T, D = int(l[2]), int(l[3])
            waiting.append([T,D])
        
        for i in range(len(waiting)):
            if(waiting[i][1] == D):
                print("ready", waiting[i][0], D)
                waiting.pop(i)
        



step = int(input())

if(step == 1):
    step1()
elif(step == 2):
    step2()
elif(step == 3):
    step3()

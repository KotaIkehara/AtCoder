import copy

V, E, X, Y = map(int, input().split())
N = list(map(int, input().split()))
M = list(map(int, input().split()))
edge = []
for i in range(E):
    a, b = map(int, input().split())
    edge.append([a, b])

experienced = set()
patient = [0]*V
time = [0]*V


# 最初から全員感染しているとき
if(V == X):
    if (max(M) <= Y):
        print(0)
    else:
        print(len([i for m in M if(m > Y)]))
    exit()

# 誰かが感染していないとき
# 時刻０：初期状態を作る
for i in range(X):
    patient[N[i]-1] = M[i]
    time[N[i] - 1] = M[i]
    experienced.add(N[i] - 1)

# 時刻１～Y
for y in range(Y):
    # 前の時刻の感染者の感染時間を１減らす
    for e in experienced:
        patient[e] -= 1
    # 感染者に隣接する人に感染する
    prevPatient = [i for i in range(V) if(patient[i] > 0)]
    prevExperienced = copy.copy(experienced)
    prevEdge = edge[:]
    for i in prevPatient:
        # 隣接者の探索
        for e in prevEdge:
            # 感染者に隣接しているか/過去に感染したかの判定
            if(i == e[0]-1 and (e[1]-1 not in prevExperienced)):
                patient[e[1]-1] = max(patient[e[1]-1], time[e[0]-1])
                time[e[1] - 1] = max(patient[e[1]-1], time[e[1]-1])
                edge.remove(e)
                experienced.add(e[1] - 1)
            if(i == e[1]-1 and (e[0]-1 not in prevExperienced)):
                patient[e[0]-1] = max(patient[e[0]-1], time[e[1]-1])
                time[e[0] - 1] = max(patient[e[0]-1], time[e[0]-1])
                edge.remove(e)
                experienced.add(e[0] - 1)

print(len([i for p in patient if(p > 0)]))

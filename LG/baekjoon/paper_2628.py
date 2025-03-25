import sys

ga , se = map(int,input().split())
n = int(input())

garo_cut = [0, ga]
sero_cut = [0, se]

# 자를 위치 저장 → 정렬 → 구간 크기 계산 
for _ in range(n):
    d, l = map(int, input().split())
    if d == 0:
        sero_cut.append(l)
    else:
        garo_cut.append(l)

garo_cut.sort()
sero_cut.sort()

max_garo = max(garo_cut[i+1] - garo_cut[i] for i in range(len(garo_cut) - 1))
max_sero = max(sero_cut[i+1] - sero_cut[i] for i in range(len(sero_cut) - 1))

print(max_garo * max_sero)

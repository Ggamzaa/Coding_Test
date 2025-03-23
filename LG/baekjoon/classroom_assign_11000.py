import sys

input = sys.stdin.readline  # 코테용 빠른 입력 처리

N = int(input())
classes = [tuple(map(int, input().split())) for _ in range(N)]

classes.sort()  # 시작 시간 기준 정렬

rooms = []  # 강의실 끝나는 시간 저장

for s, t in classes:
    placed = False
    # 현재 열려있는 강의실 순회
    for i in range(len(rooms)):
        if rooms[i] <= s:
            rooms[i] = t  # 강의실 재사용
            placed = True
            break
        
    if not placed:
        rooms.append(t)  # 새 강의실 추가

print(len(rooms))
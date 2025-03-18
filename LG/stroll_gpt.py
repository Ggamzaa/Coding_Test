import sys

input = sys.stdin.readline  # 코테용 빠른 입력 처리

# 입력
N, T = map(int, input().split())
people = [tuple(map(int, input().split())) for _ in range(N)]

# 핵심: 뒤에서부터 살펴보기 위해 출발 위치 기준 내림차순 정렬
people.sort(reverse=True)
print(people)

group_count = 0
min_arrival = float('inf')  # 가장 앞에 도착 가능한 사람 기준
print(min_arrival)

for start, speed in people:
    arrival = start + speed * T  # T분 후 최종 위치 계산
    if arrival < min_arrival:
        group_count += 1
        min_arrival = arrival  # 새 그룹 기준 업데이트
        print(min_arrival)
    # arrival >= min_arrival 이면 같은 그룹이므로 무시

print(group_count)

# 5 3
# 0 1
# 1 2
# 2 3
# 3 2
# 6 1
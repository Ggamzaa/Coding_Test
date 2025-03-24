import sys
import heapq

input = sys.stdin.readline  # 코테용 빠른 입력 처리

N = int(input())
classes = [tuple(map(int, input().split())) for _ in range(N)]

classes.sort()  # 시작 시간 기준 정렬

heap = []  # 강의실마다 수업 '끝나는 시간'만 저장할 min-heap (우선순위 큐)

for s, t in classes:
    # 현재 heap의 가장 작은 값(가장 빨리 끝나는 수업의 끝나는 시간)과 비교
    if heap and heap[0] <= s:
        # 현재 수업의 시작 시간이 가장 빨리 끝나는 수업보다 크거나 같으면 그 강의실 사용 가능
        heapq.heappop(heap)  # 가장 빨리 끝나는 강의실을 비우고
    heapq.heappush(heap, t)  # 현재 수업을 heap에 넣는다 (끝나는 시간 기준)

# heap에 남아 있는 수가 필요한 강의실 수
print(len(heap))
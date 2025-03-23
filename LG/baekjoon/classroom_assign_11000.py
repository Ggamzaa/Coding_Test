import sys
import heapq

input = sys.stdin.readline  # 코테용 빠른 입력 처리

N = int(input())
classes = [tuple(map(int, input().split())) for _ in range(N)]

classes.sort()  # 시작 시간 기준 정렬

rooms = []  # 강의실 끝나는 시간 저장

heap = []
for s, t in classes:
    if heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, t)

print(len(heap))
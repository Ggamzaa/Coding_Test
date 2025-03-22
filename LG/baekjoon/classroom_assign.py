import sys

input = sys.stdin.readline  # 코테용 빠른 입력 처리

N = map(int, input().split())
people = [tuple(map(int, input().split())) for _ in range(N)]


import sys

input = sys.stdin.readline  # 코테용 빠른 입력 처리

N = int(input())
buildings = [int(input()) for _ in range(N)]

# flag를 둬서 자신보다 크면 true => true면 다음 빌딩은 패스 후 다시 flag = false

# 하지만 이중 for문을 돌아야하나??



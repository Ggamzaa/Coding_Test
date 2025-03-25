import sys

input = sys.stdin.readline  # 코테용 빠른 입력 처리

N = int(input())
buildings = [int(input()) for _ in range(N)]

# flag를 둬서 자신보다 크면 true => true면 다음 빌딩은 패스 후 다시 flag = false

stack = []
answer = 0

for height in buildings:
    while stack and stack[-1] <= height:
        stack.pop()
    answer += len(stack)
    stack.append(height)

print(answer)
# 하지만 이중 for문을 돌아야하나??




n = int(input())
heights = list(map(int,input().split()))

stack = []
result = []

for i in range(n):
    # 현재 탑의 높이
    current_height = heights[i]

    # 스택에서 나보다 낮은 탑은 제거
    while stack and stack[-1][1] < current_height:
        stack.pop()
    
    # 스택이 비었으면 0, 아니면 스택의 top이 레이저가 닿는 탑
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][0] + 1)  # 인덱스는 1부터 시작하므로 +1

    # 현재 탑을 스택에 넣음

    stack.append((i, current_height))

print(' '.join(map(str, result)))
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

'''
뒤에서 부터 숫자들을 읽어서 자신보다 오른쪽에 잇는 수들 중 가장 큰수를 업데이트 해가는 방식
숫자들을 어떻게 뒤에서부터 읽지...?
근데 큰수들중에 가장 왼쪽에 있는거면 그리디....?
'''
result = [-1] * n  # 결과 리스트, 처음에는 모두 -1로 초기화
stack = []  # 스택 초기화

for i in range(n):
    # 스택이 비어있지 않고, 현재 원소가 스택의 top에 있는 원소보다 클 경우
    while stack and arr[stack[-1]] < arr[i]:
        idx = stack.pop()  # 해당 인덱스 원소는 오큰수가 발견됨
        result[idx] = arr[i]  # 오큰수로 현재 원소를 저장
    
    # 현재 원소의 인덱스를 스택에 추가
    stack.append(i)

print(*result)
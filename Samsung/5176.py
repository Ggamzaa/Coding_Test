#import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")
def inorder(node):
    global value
    if node <= N:
        inorder(node * 2)              # 왼쪽 자식 방문
        tree[node] = value             # 현재 노드에 값 할당
        value += 1
        inorder(node * 2 + 1)          # 오른쪽 자식 방문

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())                    # 총 노드 수
    tree = [0] * (N + 1)                # 인덱스 1번부터 시작
    value = 1                           # 트리에 저장할 값 (1~N)

    inorder(1)                          # 루트는 항상 노드 1번

    print(f"#{test_case} {tree[1]} {tree[N//2]}")
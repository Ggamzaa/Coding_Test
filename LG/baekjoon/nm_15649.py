import sys

input = sys.stdin.readline

n,m= map(int,input().split())

visited = [False] * (n + 1)
result = []

def dfs(depth):                                                                                                                                                                    
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(depth + 1)
            visited[i] = False
            result.pop()

dfs(0)
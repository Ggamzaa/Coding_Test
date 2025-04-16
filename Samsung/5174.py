def count_nodes(node):
    cnt = 1  # 자기 자신 포함
    for child in tree.get(node, []):
        cnt += count_nodes(child)
    return cnt

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    
    tree = {}
    for i in range(0, len(data), 2):
        parent = data[i]
        child = data[i+1]
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)
    
    result = count_nodes(N)
    print(f"#{tc} {result}")
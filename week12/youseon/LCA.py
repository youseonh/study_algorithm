import sys

sys.setrecursionlimit(100000)

N = int(input())  # 노드의 개수

parent = [0] * (N + 1)  # 각 노드의 부모 노드 정보
d = [0] * (N + 1)  # 각 노드까지의 깊이
visited = [0] * (N + 1)  # 방문 여부
graph = [[] for _ in range(N + 1)]  # 트리 그래프

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# 깊이 저장
def dfs(x, depth):
    visited[x] = True
    d[x] = depth
    for node in graph[x]:
        if visited[node]:
            continue
        parent[node] = x
        dfs(node, depth + 1)


dfs(1, 0)

m = int(input())


# 최소 공통 조상 찾기(a와 b의 공통 조상)
def lca(a, b):
    # 깊이 맞추기 (같아질때까지 진행)
    while d[a] != d[b]:
        # a의 깊이가 더 깊으면 a를 a의 부모로 변경
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    # a와 b의 깊이가 같아지면 노드 맞추기
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))

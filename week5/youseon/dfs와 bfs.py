from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)


def DFS(v):
    dfs_visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not dfs_visited[i]:
            DFS(i)


def BFS(v):
    queue = deque([v])
    bfs_visited[v] = True
    while queue:  # 더이상 큐에 아무것도 남아 있지 않을때까지 반복
        pop = queue.popleft()
        print(pop, end=' ')
        for i in graph[pop]:
            if not bfs_visited[i]:
                queue.append(i)  # 방문할 때 큐에 넣기
                bfs_visited[i] = True


DFS(v)
print() # print 없으면 같은 줄에 출력됨
BFS(v)
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline
#  컴퓨터의 수
n = int(input())
# 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(value):
    visited[value] = True
    for v in graph[value]:
        if visited[v] == False:
            dfs(v)

dfs(1)
print(visited.count(True)-1)
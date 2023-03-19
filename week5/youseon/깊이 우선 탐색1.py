import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(value):
    global cnt
    visited[value] = cnt    

    for v in graph[value]:
        if visited[v] == 0:
            cnt += 1
            dfs(v)

cnt = 1

# 정점의 수, 간선의 수, 정점 시작 번호
N, M, R = map(int, input().split()) # 5 5 1
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1) # 방문 여부 확인 (일단 방문 안한 0으로 초기화)

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)    
    graph[s].sort() # 정렬 - 문제에서 오름차순 정렬 조건

print(graph) # [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []]

# 함수 시작
dfs(R)

for _ in range(1, N+1):
    print(visited[_])
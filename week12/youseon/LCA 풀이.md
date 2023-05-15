[11437번: LCA](https://www.acmicpc.net/problem/11437)

## 문제

### 문제 설명

N(2 ≤ N ≤ 50,000)개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다.

두 노드의 쌍 M(1 ≤ M ≤ 10,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

### 입력

첫째 줄에 노드의 개수 N이 주어지고, 다음 N-1개 줄에는 트리 상에서 연결된 두 정점이 주어진다. 그 다음 줄에는 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M이 주어지고, 다음 M개 줄에는 정점 쌍이 주어진다.

### 출력

M개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상을 출력한다.

### 예제 입력 1

```
15
1 2
1 3
2 4
3 7
6 2
3 8
4 9
2 5
5 11
7 13
10 4
11 15
12 5
14 7
6
6 11
10 9
2 6
7 6
8 13
8 15

```

### 예제 출력 1

```
2
4
2
1
3
1

```

## 알고리즘

- LCA
- BFS

## 제출 코드

- 이전에 LCA알고리즘을 사용, 응용하는 문제를 풀 때 아예 알고리즘 개념을 몰라서 많이 헤매서 아예 알고리즘 기초 문제를 풀어봄
- 기본적인 문제 풀이 단계를 외우는 것이 중요한듯
    1. 모든 노드의 깊이를 구하고 해당 노드의 부모정보를 저장하기
    2. 비교하려는 노드의 깊이를 같아지도록 맞추고 부모 정보가 같아질 때까지 부모정보 저장하면서 같아지면 리턴하기

```bash
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
```
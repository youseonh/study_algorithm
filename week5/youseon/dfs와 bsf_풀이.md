## 문제

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

### 입력

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

### 출력

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

### 예제 입력 1

```
4 5 1
1 2
1 3
1 4
2 4
3 4

```

### 예제 출력 1

```
1 2 4 3
1 2 3 4

```

### 예제 입력 2

```
5 5 3
5 4
5 2
1 2
3 4
3 1

```

### 예제 출력 2

```
3 1 2 5 4
3 1 4 2 5

```

### 예제 입력 3

```
1000 1 1000
999 1000

```

### 예제 출력 3

```
1000 999
1000 999

```

## 알고리즘

- [그래프 이론](https://www.acmicpc.net/problem/tag/7)
- [그래프 탐색](https://www.acmicpc.net/problem/tag/11)
- [너비 우선 탐색](https://www.acmicpc.net/problem/tag/126)
- [깊이 우선 탐색](https://www.acmicpc.net/problem/tag/127)

## 제출 코드

- 몇 부분이 헷갈리는 부분이 있지만 DFS는 어느정도 개념을 숙지함
- BFS는 할때마다 헷갈림..

```python
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
```
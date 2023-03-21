# DFS와 BFS

---

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

### 입력

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

### 출력

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

---

## 제출코드

```
public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());
    int V = Integer.parseInt(st.nextToken());

    int[][] adjMatrix = new int[N + 1][N + 1];

    for (int i = 0; i < M; i++) {
        st = new StringTokenizer(br.readLine());
        int to = Integer.parseInt(st.nextToken());
        int from = Integer.parseInt(st.nextToken());
        adjMatrix[to][from] = 1; //무향 그래프이므로 양쪽에 다 넣어주기
        adjMatrix[from][to] = 1;
    }
    dfs(V, new boolean[N + 1], N, adjMatrix);
    System.out.println();
    // bfs
    bfs(V, N, adjMatrix);
}

private static void dfs(int v, boolean[] selected, int N, int[][] adjMatrix) {
    selected[v] = true;
    System.out.print(v + " ");
    for (int i = 1; i <= N; i++) {
        if (adjMatrix[v][i] == 1 && !selected[i]) dfs(i, selected, N, adjMatrix);
    }
}

private static void bfs(int start, int N, int[][] adjMatrix) {
    Queue<Integer> queue = new LinkedList<>();
    boolean[] selected = new boolean[N + 1];
    queue.offer(start);
    selected[start] = true;
    while (!queue.isEmpty()) {
        int temp = queue.poll();
        System.out.print(temp + " ");
        for (int i = 1; i <= N; i++) {
            if (adjMatrix[temp][i] == 1 && !selected[i]) {
                queue.offer(i);
                selected[i] = true;
            }
        }
    }
}

```
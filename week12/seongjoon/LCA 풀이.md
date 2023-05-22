# LCA

---

N(2 ≤ N ≤ 50,000)개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다.

두 노드의 쌍 M(1 ≤ M ≤ 10,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

### 입력

첫째 줄에 노드의 개수 N이 주어지고, 다음 N-1개 줄에는 트리 상에서 연결된 두 정점이 주어진다. 그 다음 줄에는 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M이 주어지고, 다음 M개 줄에는 정점 쌍이 주어진다.

### 출력

M개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상을 출력한다.

---

## 제출코드

```
static int N, M;
static int[] parent;
static int[] depth;
static boolean[] visited;
static Node[] graph;
static StringTokenizer st;

static class Node {
    int vertex;
    Node link;

    public Node(int vertex, Node link) {
        super();
        this.vertex = vertex;
        this.link = link;
    }
}

public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    N = Integer.parseInt(br.readLine());
    parent = new int[N + 1];
    depth = new int[N + 1];
    visited = new boolean[N + 1];
    graph = new Node[N + 1];

    for (int i = 1; i < N; i++) {
        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        graph[start] = new Node(end, graph[start]);
        graph[end] = new Node(start, graph[end]);
    }
    dfs(1, 0);

    M = Integer.parseInt(br.readLine());
    for (int i = 0; i < M; i++) {
        st = new StringTokenizer(br.readLine());
        sb.append(lca(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        sb.append("\n");
    }
    System.out.println(sb.toString());

}

static void dfs(int v, int d) {
    visited[v] = true;
    depth[v] = d;

    for (Node temp = graph[v]; temp != null; temp = temp.link) {
        if (!visited[temp.vertex]) {
            parent[temp.vertex] = v;
            dfs(temp.vertex, d + 1);
        }
    }
}

static int lca(int a, int b) {
    while (depth[a] != depth[b]) {
        if (depth[a] > depth[b])
            a = parent[a];
        else
            b = parent[b];
    }

    while (a != b) {
        a = parent[a];
        b = parent[b];
    }
    return a;
}
```
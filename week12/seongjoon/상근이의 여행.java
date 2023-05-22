import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class 상근이의 여행 {

    private static int n, m;
    private static int cnt;
    private static ArrayList<Integer>[] list;
    private static boolean[] visit;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        while (t-- > 0) {
            st = new StringTokenizer(reader.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            list = new ArrayList[n + 1];
            visit = new boolean[n + 1];

            for (int i = 0; i <= n; i++) {
                list[i] = new ArrayList<>();
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(reader.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                list[a].add(b);
                list[b].add(a);
            }
            sb.append(n - 1 + "\n");
        }
        System.out.print(sb);
    }

}

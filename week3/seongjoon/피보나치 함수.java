import java.util.Scanner;

public class 피보나치 함수 {

    static Integer[][] dp = new Integer[41][2];

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        dp[0][0] = 1;
        dp[0][1] = 0;
        dp[1][0] = 0;
        dp[1][1] = 1;
        int T = in.nextInt();
        while (T-- > 0) {
            int N = in.nextInt();
            fibonacci(N);
            System.out.println(dp[N][0] + " " + dp[N][1]);
        }
    }

    static Integer[] fibonacci(int N) {
        if (dp[N][0] == null || dp[N][1] == null) {
            dp[N][0] = fibonacci(N - 1)[0] + fibonacci(N - 2)[0];
            dp[N][1] = fibonacci(N - 1)[1] + fibonacci(N - 2)[1];
        }
        return dp[N];
    }

}
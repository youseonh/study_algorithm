package study.week5;

import java.io.*;

// DP
public class 알고리즘 수업 - 피보나치 수 1 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        //코드 1은 1을 더한 횟수임으로 피보나치수와 동일
        //코드 2는 3~n만큼 반복이므로 n-2만큼 실행
        bw.append(String.valueOf(fibonacci(n))).append(" ").append(String.valueOf(n - 2));
        bw.close();
        br.close();
    }

    //dp를 이용한 피보나치 수 출력
    public static int fibonacci(int n) {
        int[] fibos = new int[n + 1];
        fibos[1] = fibos[2] = 1;
        for (int i = 3; i <= n; i++) {
            fibos[i] = fibos[i - 1] + fibos[i - 2];
        }
        return fibos[n];
    }

}

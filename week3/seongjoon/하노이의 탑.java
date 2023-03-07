
public class 하노이의 탑 {

    public int[][] solution(int n) {
        int num = (n + n) - 1;
        int[][] answer = new int[num][2];
        for (int i = 0; i < num; i++) {
            int count = 1;
            for (int j = 0; j < 2; j++) {
                if (i == n - 1) {
                    answer[i][j] = count;
                    count += 2;
                } else if (i >= n) {
                    answer[i][j] = count + 1;
                    count += 1;
                } else {
                    answer[i][j] = count;
                    count += 1;
                }
            }
        }
        return answer;
    }

}
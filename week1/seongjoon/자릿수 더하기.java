package study.week2

public class 자릿수 더하기 {

    public static int solution(int n) {
        int sum = 0;
        while (n > 0) {
            int number = n % 10;
            sum += number;
            n /= 10;
        }
        return sum;
    }

}
import java.util.ArrayList;
import java.util.List;

public class 약수의 개수와 덧셈 {

    public int solution(int left, int right) {
        int sum = 0;
        for (int i = left; i <= right; i++) {
            List<Integer> divisors = new ArrayList<>();
            for (int j = 1; j <= i; j++) {
                if (i % j == 0) {
                    divisors.add(i);
                }
            }
            if (divisors.size() % 2 == 0) {
                sum += i;
            } else {
                sum -= i;
            }
        }
        return sum;
    }

}

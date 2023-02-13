import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Q1 {

    public List<Integer> solution(int N, int[] stages) {
        List<Integer> answer = new ArrayList<>();
        List<Double> failureProbability = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            double a = 0;
            double b = 0;
            for (int num : stages) {
                if (i + 1 == num) {
                    a++;
                }
                if (i + 1 <= num) {
                    b++;
                }
            }
            if (a == 0 && b == 0) {
                failureProbability.add(i, 0.0);
            } else {
                failureProbability.add(i, a / b);
            }
        }

        int count = 0;
        for (int i = 0; i < N; i++) {
            if (count >= 1) {
                count--;
                continue;
            }
            double max = -1;
            int maxIndex = 0;
            for (int j = 0; j < failureProbability.size(); j++) {
                if (max < failureProbability.get(j)) {
                    max = failureProbability.get(j);
                    maxIndex = j;
                }
            }
            List<Integer> maxIndexValues = new ArrayList<>();
            for (int j = 0; j < failureProbability.size(); j++) {
                if (max == failureProbability.get(j) && maxIndex != j) {
                    maxIndexValues.add(j);
                    count++;
                }
            }
            if (maxIndexValues.size() == 0) {
                answer.add(maxIndex + 1);
            } else {
                maxIndexValues.add(maxIndex);
                Collections.sort(maxIndexValues);
                for (int num : maxIndexValues) {
                    answer.add(num + 1);
                }
            }
            for (int j = 0; j < failureProbability.size(); j++) {
                if (max == failureProbability.get(j)) {
                    failureProbability.set(j, (double) -2);
                }
            }
        }
        return answer;
    }

}
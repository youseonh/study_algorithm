def solution(numbers):
    answer = set()
    for idx in range(0, len(numbers)-1):
        for i in range(idx, len(numbers)-1):
            result = numbers[idx] + numbers[i+1]
            answer.add(result)
            
    answer = list(answer)
    answer.sort()
    return answer
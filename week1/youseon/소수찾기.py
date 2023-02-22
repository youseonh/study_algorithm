def solution(n):
    # 1. answer 에 set()자료형으로 2~n까지의 정수 저장
    answer = set(range(2, n+1))
    # 2. 2 ~ n까지 answer에 i 가 있다면 n까지의 수 중 i의 배수를 모두 제거
    for i in range(2,n+1):
        if i in answer:
            answer -= set(range(i*2, n+1, i))
    return len(answer)
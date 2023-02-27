import heapq
# heapQ를 사용하지 않을 경우 sort를 사용할 수 있는데, 시간 초과가 발생한다.
    # heapq.heapify(list) #기존의 리스트를 오름차순 heapQ로 변환
    # heapq.heappop(list) #list의 가장 작은 값을 return하며 삭제
    # heapq.heappush(list, value) #list에 value를 삽입, 자동으로 정렬한다
    
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K: #가장 작은 수가 기준보다 낮다면 계속
        if len(scoville)>1:
            answer += 1
            first = heapq.heappop(scoville) 
            second = heapq.heappop(scoville) 
            heapq.heappush(scoville, first + second *2)
        else:
            return -1
    return answer
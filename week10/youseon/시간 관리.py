import sys

if __name__ == '__main__':
    N = int(input()) # 일의 수 N
    arr = []
    for _ in range(N):
        # 일에 대한 Ti와 Si (Ti 시간이 걸리고 Si 시 내에 이 일을 처리하여야 한다)
        a, b = map(int, sys.stdin.readline().split()) 
        arr.append((b, a))
    # 가장 늦은 시간에 해결해도 되는 일 순서대로 정렬
    arr.sort(reverse=True)
    ans = arr[0][0] - arr[0][1] # ans 일단 초기화

    for i in range(1, N):
        # i번째 일을 끝마쳐야 하는 시간이 현재 시간보다 앞선다면
        # 시작 시간 갱신 : i번째 일을 시작할 수 있는 가장 늦은 시간
        if ans > arr[i][0]:
            ans = arr[i][0] - arr[i][1]
        # i번째 일을 끝마쳐야 하는 시간이 현재 시간보다 앞서지 않는다면
        # 시작 시간 갱신 : i번쨰 일을 완료하는데 걸리는 시간만큼 현재 시간에서 감소
        else:
            ans -= arr[i][1]
    print(ans if ans >= 0 else -1)
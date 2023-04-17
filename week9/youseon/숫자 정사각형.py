N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

max_size = min(N, M)  # 최대 정사각형의 크기
ans = 1  # 가장 큰 정사각형의 넓이

# 2부터 최대 정사각형의 크기까지 반복하면서 각각의 크기에 대한 모든 정사각형을 확인
for k in range(2, max_size+1):
    for i in range(N-k+1):
        for j in range(M-k+1):
						# 이전에 구한 가장 큰 정사각형의 넓이와 비교하여 더 큰 값을 저장
            if arr[i][j] == arr[i+k-1][j] == arr[i][j+k-1] == arr[i+k-1][j+k-1]:
                ans = max(ans, k*k)

print(ans)
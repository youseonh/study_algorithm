def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:  # 첫번째일때 윗줄 첫번째 선택해서 더함
                triangle[i][j] += triangle[i - 1][j]
            elif j == i:  # 마지막일때 윗줄 마지막에서 -1번째 선택해서 더함
                triangle[i][j] += triangle[i - 1][j - 1]
            else:  # 둘 중에 큰거 선택해서 더함
                triangle[i][j] += max(triangle[i - 1][j],
                                      triangle[i - 1][j - 1])
    return max(triangle[-1])

n = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(n))
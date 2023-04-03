import sys

# N x N 크기의 행렬 A와 B를 입력으로 받음
n, b = map(int, sys.stdin.readline().split())
A = []
for _ in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

# 행렬 곱셈 함수
def mul(n, a, b):
    result = [[0] * n for _ in range(n)] # 결과 행렬 초기화
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000 # 오버플로우 방지를 위해 1000으로 나눈 나머지 사용
    return result

# 행렬 A의 B제곱을 계산하는 함수
def matrix_pow(n, b, A):
    # B가 1일 때 A를 그대로 반환
    if b == 1:
        return A
    # B가 2일 때 A*A를 반환
    elif b == 2:
        return mul(n, A, A)
    # B가 홀수일 때는 A*A^(B-1)을 계산
    elif b % 2 == 1:
        return mul(n, A, matrix_pow(n, b-1, A))
    # B가 짝수일 때는 (A^(B/2))^2를 계산
    else:
        temp = matrix_pow(n, b//2, A)
        return mul(n, temp, temp)

# 행렬 A의 B제곱을 계산하여 출력
result = matrix_pow(n, b, A)
for row in result:
    for num in row:
        print(num % 1000, end=' ')
    print()
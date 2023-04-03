from sys import stdin, stdout

n = stdin.readline()
# 미리 정렬
N = sorted(map(int, stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())


# 이분 탐색
def binary(l, N, start, end):
    if start > end:
        return 0
    # 중간 지점의 인덱스
    m = (start + end) // 2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m - 1)
    else:
        return binary(l, N, m + 1, end)


# 찾을 숫자 l, 배열 N
for l in M:
    start = 0
    end = len(N) - 1
    print(binary(l, N, start, end))
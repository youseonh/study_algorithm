import sys

def binary_search(target, start, end, cards):
    if start > end:
        return 0

    mid = (start + end) // 2
    if cards[mid] == target:
        return 1
    elif cards[mid] > target:
        return binary_search(target, start, mid - 1, cards)
    else:
        return binary_search(target, mid + 1, end, cards)

# 상근이가 가지고 있는 카드의 개수
n = int(input())
cards = list(map(int, sys.stdin.readline().split()))

# 카드 정렬
cards.sort()

# 비교할 카드의 개수
m = int(input())
targets = list(map(int, sys.stdin.readline().split()))

for target in targets:
    result = binary_search(target, 0, n - 1, cards)
    print(result, end=' ')
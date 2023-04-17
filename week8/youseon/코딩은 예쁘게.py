n = int(input())
s, e = list(map(int, input().split())), list(map(int, input().split()))
diff = list(x - y for x, y in zip(s, e))
isBiggerZero = diff[0] > 0
tmp = []
answer = 0


def countIntent(x):
    if len(x) == 0:
        return 0
    elif len(x) == 1:
        return x[0]
    else:
        minValue = min(x)
        idx = x.index(minValue)
        cnt = minValue
        cnt += max(0, countIntent(x[:idx]) - minValue)
        cnt += max(0, countIntent(x[idx + 1:]) - minValue)
    return cnt


for x in diff:
    print(x, isBiggerZero)
    if (x > 0) == isBiggerZero:
        tmp.append(abs(x))
    else:
        op = not isBiggerZero
        answer += countIntent(tmp)
        tmp = [abs(x)]

answer += countIntent(tmp)

print(answer)

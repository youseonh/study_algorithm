count = 1
isPossible = True
stack = []
arr = []

N = int(input())
for i in range(N):
    num = int(input())
    while count <= num:
        stack.append(count)
        arr.append('+')
        count += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        arr.append('-')
    else:
        isPossible = False
        break
        
## 확인
if isPossible == False:
    print("NO")
else:
    for i in arr:
        print(i)
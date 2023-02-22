def solution(n):
    answer = 0
    str_num = format(n)
    for index in range(0, len(str_num)):
        answer += int(str_num[index])

    return answer
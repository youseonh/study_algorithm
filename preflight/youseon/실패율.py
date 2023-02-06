def solution(N, stages):
    stage_set = {}
    answer = []
    total_user = len(stages)
    for stage_num in range(1, N + 1):
        # 더이상 스테이지가 남아있지 않을 때
        if len(stages) == 0: stage_set[stage_num] = 0
        else:
            fail_cnt = stages.count(stage_num)
            # 마지막 스테이지
            if stage_num == N + 1:
                fail_cnt = stages.count(stage_num) + stages.count(stage_num +
                                                                  1)
            stage_set[stage_num] = fail_cnt / len(stages)
        # 계산한 스테이지 제거
        remove_set = {stage_num}
        stages = [i for i in stages if i not in remove_set]

    sorted_list = sorted(stage_set.items(), key=lambda x: x[1], reverse=True)
    for num in sorted_list:
        answer.append(num[0])
    return answer


print(solution(4, [1, 2, 3, 2, 1]))
# return = [3, 2, 1, 4]
print(solution(5, [3,3,3,3]))
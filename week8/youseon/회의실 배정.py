n = int(input())  # 회의의 수

meetings = []  # 회의 정보를 저장할 리스트
for i in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간을 기준으로 오름차순 정렬

count = 0  # 선택한 회의의 수
end_time = 0  # 회의가 끝나는 시간
for start, end in meetings:
    if start >= end_time:  # 회의가 끝나는 시간 이후에 시작하는 경우
        count += 1
        end_time = end

print(count)  # 선택한 회의의 수 출력
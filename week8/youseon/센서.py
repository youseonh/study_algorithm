n = int(input())  # 센서의 개수
k = int(input())  # 구간의 개수

if k >= n:  # 구간의 개수가 센서의 개수보다 크거나 같으면 0 출력
    print(0)
else:
    sensors = list(map(int, input().split()))
    sensors.sort()  # 센서를 오름차순으로 정렬

    dists = []  # 인접한 센서들 간의 거리를 저장할 리스트
    for i in range(1, n):
        dists.append(sensors[i] - sensors[i-1])  # 인접한 센서들 간의 거리 계산

    dists.sort(reverse=True)  # 거리를 내림차순으로 정렬

    for i in range(k-1):  # 가장 긴 거리들부터 K-1번 자르기
        dists[i] = 0

    print(sum(dists))  # 자른 거리들의 합 출력
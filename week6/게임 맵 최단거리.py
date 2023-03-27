from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[False]* m for _ in range(n)]

    # 동, 서, 남, 북
    position_x = [1,-1,0,0]
    position_y = [0,0,1,-1]

    queue = deque()
    queue.append((0,0)) # 시작
    visited[0][0]=True

    while queue:
        y, x = queue.popleft()

        # 동서남북 확인
        for i in range(4):
            nx = x + position_x[i]
            ny = y + position_y[i]
            # 벽이 아니고 1인 경우 확인
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    maps[ny][nx] = maps[y][x]+1
    if maps[n-1][m-1]==1:
        return -1
    else:
        return maps[n-1][m-1]
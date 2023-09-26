from collections import deque

def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            # 큐에서 하나의 원소를 뽑아 출력
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 현재 위치에서 네 방향으로의 위치 확인
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                # 벽인 경우
                if maps[nx][ny] == 0:
                    continue
                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    
        return maps[len(maps) - 1][len(maps[0]) - 1]
    
    answer = bfs(0, 0)
    return -1 if answer == 1 else answer
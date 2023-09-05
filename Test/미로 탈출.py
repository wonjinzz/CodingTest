from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
def bfs(x, y):
    queue = deque()
    graph.append((x, y))
    
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
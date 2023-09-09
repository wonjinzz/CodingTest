from collections import deque # deque 사용하기 위해

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
N, M, K, X = map(int, input().split())

city = [[] for _ in range(N + 1)] # N개의 도시 개수

# M개의 도로 정보 입력
for _ in range(M):
    A, B = map(int, input().split())
    city[A].append(B)
    
distance = [-1] * (N + 1) # 모든 도시에 대한 최단 거리 초기화
distance[X] = 0 # 출발 도시까지의 거리는 0으로 설정

# BFS
queue = deque([X])
# 큐가 빌 때까지 반복
while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    # 현재 도시에서 이동 가능한 도시 확인
    for next in city[v]:
        # 방문하지 않은 도시라면
        if distance[next] == -1:
            distance[next] = distance[v] + 1
            queue.append(next)
            
# 최대한 거리가 K인 모든 도시의 번호를 오름차순으로 정렬
check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

# 최단 거리가 K인 도시가 하나도 존재하지 않으면 
if check == False:
    print(-1)
            
def solution(cacheSize, cities):
    # Cache Hit: CPU 가 참조하고자 하는 메모리가 캐시에 존재하고 있을 경우
    # Cache Miss: CPU 가 참조하고자 하는 메모리가 캐시에 존재하지 않을 경우
    answer = 0
    cache = []

    if not cacheSize: # 캐시사이즈가 0이라면
        return len(cities) * 5
        
    for c in cities:
        c = c.lower() # 입출력 예제를 보면 대소문자 훼이크 있어서 다 소문자로 변환
        if c not in cache:
            answer += 5 # cache miss
            if len(cache) < cacheSize: # 캐시크기 안
                cache.append(c)
            else: # 캐시 크기보다 클 때
                cache.pop(0)
                cache.append(c)
        else:
            answer += 1 # cache hit
            if len(cache) < cacheSize:
                cache.append(c)
            else: 
                cache.remove(c)
                cache.append(c)
            
    return answer

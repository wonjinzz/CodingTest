import math # 반올림 하기 위함

def solution(fees, records):
    answer = []
    in_ = dict() # 차량의 입차 시간을 저장하기 위한 딕셔너리
    fee = dict() # 차량의 주차 요금을 저장하기 위한 딕셔너리
    
    for x in records:
        a, b, c = x.split() # 입/출차 기록
        h, m = a.split(':') # 시:분
        time = int(h) * 60 + int(m) # 시간을 분 단위로 계산
        
        if c == 'IN':
            in_[b] = time # 차량이 입차한 시간을 기록
        else:
            fee[b] = fee.get(b, 0) + (time - in_[b]) # 차량의 주차 요금 계산 및 저장
            del in_[b] # 입차 기록 삭제
            
    for x in in_: # 아직 주차장에 있는 차량들에 대한 주차 요금 계산
        fee[x] = fee.get(x, 0) + 23 * 60 + 59 - in_[x]
        
    for x, y in sorted(fee.items()): # 차량 번호를 정렬하여 순회
        if y > fees[0]: # 무료 주차 시간을 초과한 경우
            # 기본 요금(fees[1])에 추가 요금을 더하여 계산하고 결과를 리스트에 추가
            answer.append(fees[1] + math.ceil((y - fees[0]) / fees[2]) * fees[3])
        else:
            answer.append(fees[1]) # 무료 주차 시간인 경우 기본 요금만
            
    return answer
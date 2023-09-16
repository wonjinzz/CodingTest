def solution(board, moves):
    answer = 0
    basket = [] # 바구니
    
    for i in moves:
        for j in range(len(board)):
            # 잡히지 않은 경우
            if board[j][i - 1] == 0:
                continue
            # 잡히는 경우
            else:
                # 잡은 인형은 basket에 삽입
                basket.append(board[j][i - 1])
                # 잡힌 인형의 위치를 0으로 change
                board[j][i - 1] = 0
                
                # 바구니에 인형이 두개 이상일 때
                if len(basket) >= 2:
                    # 뒤에서부터 두개가 같다면
                    if basket[-1] == basket[-2]:
                        basket.pop(-1)
                        basket.pop(-1)
                        answer += 2
            break
            
    return answer
def solution(survey, choices):
    answer = ''
    
    mbti = { 'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0 }
    
    for i in range(len(survey)):
        if choices[i] == 1:
            mbti[survey[i][0]] += 3
        elif choices[i] == 2:
            mbti[survey[i][0]] += 2
        elif choices[i] == 3:
            mbti[survey[i][0]] += 1
        elif choices[i] == 5:
            mbti[survey[i][1]] += 1
        elif choices[i] == 6:
            mbti[survey[i][1]] += 2
        elif choices[i] == 7:
            mbti[survey[i][1]] += 3
            
    answer += 'R' if mbti['R'] >= mbti['T'] else 'T'
    answer += 'C' if mbti['C'] >= mbti['F'] else 'F'
    answer += 'J' if mbti['J'] >= mbti['M'] else 'M'
    answer += 'A' if mbti['A'] >= mbti['N'] else 'N'
    
    return answer
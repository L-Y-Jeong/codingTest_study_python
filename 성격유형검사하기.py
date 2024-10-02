def solution(survey, choices):
    answer = []
    dict = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J':0, 'M':0, 'A':0, 'N':0}
    cnt = 0
    for sur in survey :
        s = list(sur)
        
        if choices[cnt] < 4 :
            dict[s[0]] += 4 - choices[cnt]
        elif choices[cnt] > 4 :
            dict[s[1]] += choices[cnt] - 4
        cnt += 1
            
    answer.append('R' if dict['R'] >= dict['T'] else 'T')
    answer.append('C' if dict['C'] >= dict['F'] else 'F')
    answer.append('J' if dict['J'] >= dict['M'] else 'M')
    answer.append('A' if dict['A'] >= dict['N'] else 'N')
    
    
    return ''.join(answer)

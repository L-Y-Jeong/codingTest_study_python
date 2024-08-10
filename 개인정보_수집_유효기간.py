def solution(today, terms, privacies):

    #today :split해서 나눠서 저장하기
    #terms :split해서 딕셔너리로 저장하기
    #privacies :split해서 나눠서 저장하기
    #terms의 key에서 찾아 날짜 더하기
    #today보다 크면 result에 저장
    
    answer = []
    today_y, today_m, today_d = map(int, today.split('.'))
    
    # 약관 종류와 유효기간을 딕셔너리로 저장
    termsDic = {}
    for term in terms:
        term_type, term_n = term.split()
        termsDic[term_type] = int(term_n)
    
    for j, privacy in enumerate(privacies):
        pri_date, pri_t = privacy.split()  #날짜,약관 분리
        pri_y, pri_m, pri_d = map(int, pri_date.split('.'))
    
        add_m = termsDic[pri_t]
        pri_m += add_m
        
        # 12월 초과하면 년도 추가
        if pri_m > 12:
            pri_y += (pri_m - 1) // 12
            pri_m = (pri_m - 1) % 12 + 1
        
        # 오늘 날짜랑 비교
        if (pri_y < today_y) or (pri_y == today_y and pri_m < today_m) or (pri_y == today_y and pri_m == today_m and pri_d <= today_d):
            answer.append(j + 1)
    
    return answer

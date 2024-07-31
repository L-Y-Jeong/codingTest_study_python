def solution(keymap, targets):
    answer = []
    tarDic = {}
    
    for i in keymap:
        for j in range(len(i)):
            if i[j] in tarDic: #targets 안에 key 값이 있는지 확인
                if tarDic[i[j]] > j+1: 
                    tarDic[i[j]] = j+1
                else:
                    continue
            else:
                tarDic[i[j]] = j+1
    for i in targets:
        cnt = 0
        for j in i:
            if j not in tarDic: # 아예 없으면 -1 반환
                cnt = -1
                break
            else:
                cnt += tarDic[j] #있으면 추가
        answer.append(cnt)
        
        
    return answer

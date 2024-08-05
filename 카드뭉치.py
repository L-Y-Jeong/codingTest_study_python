def solution(cards1, cards2, goal):
    cnt1 = 0
    cnt2 = 0
    for word in goal:
        if cnt1 < len(cards1) and (cards1[cnt1] == word) :
            cnt1 = cnt1 + 1
            continue
        elif cnt2 < len(cards2) and (cards2[cnt2] == word ):
            cnt2 = cnt2 +1
            continue
        else :
            return "No"
            break
        
    return "Yes"

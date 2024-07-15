#선물을 주고받는 횟수를 3개로 제한하는 것만 
추가되었기 때문에 기존 문제에서 코드 한줄만 추가하면 될 듯 하다.

def solution(friends, gifts):
    n = len(friends)
    friendArr = {friends[i]: i for i in range(n)} #이름과 순서 매핑
    giftsArr = [[0] * n for _ in range(n)] # 2차원 배열
    giveNum = [0] * n #각 보낸 선물 수
    getNum = [0] * n #각 받은 선물 수

    for i in gifts:
        send, receive = i.split()
        sendVal = friendArr[send]
        receiveVal = friendArr[receive]
        if giftsArr[sendVal][receiveVal] <= 3 :   
            giftsArr[sendVal][receiveVal] += 1 #2차원 배열 채워
            giveNum[sendVal] += 1 #보낸 선물 지수 계산
            getNum[receiveVal] += 1 #받은 선물 지수 계산

    answer = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            if giftsArr[i][j] > giftsArr[j][i]: #선물 준 수 > 선물 받은 수
                cnt += 1 #다음달에 받을 선물 수 카운트++
            elif giftsArr[i][j] == giftsArr[j][i]: #주고받은 수 같을 때 
                if giveNum[i] - getNum[i] > giveNum[j] - getNum[j]: #선물지수 비교
                    cnt+=1
        answer = max(answer, cnt) #max 갱신

    return answer

def main():
    friends = ["muzi", "ryan", "frodo", "neo"]
    gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

    result = solution(friends, gifts)
    
    print(result)

main()

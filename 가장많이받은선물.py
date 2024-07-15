#1. gifts배열은 split으로 쪼개서 사용
#2. 딕셔너리 이용해서 2차원 배열 채워넣기(행=준 사람, 열=받은 사람)
#3. 선물지수 계산
#4. 2차원배열 이용해서 비교, 같으면 선물지수도 비교 후 cnt 세기

def solution(friends, gifts):
    n = len(friends)
    friendArr = {friends[i]: i for i in range(n)} #이름과 숫자 매핑
    giftsArr = [[0] * n for _ in range(n)] #2차원배열 생성
    giveNum = [0] * n #각 보낸 선물 수
    getNum = [0] * n #각 받은 선물 수
        
    for i in gifts:
        send, receive = i.split() #gifts에서 공백으로 분리 후 삽입
        sendVal = friendArr[send] #send(이름)의 인덱스 찾아서 값 넣음
        receiveVal = friendArr[receive]
        giftsArr[sendVal][receiveVal] += 1 #2차원 배열 채워넣어
        giveNum[sendVal] += 1 #보낸 선물 수 증가
        getNum[receiveVal] += 1 #받은 선물 수 증가
    
    answer = 0
    
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            if giftsArr[i][j] > giftsArr[j][i]: #선물 준 수 > 선물 받은 수
                cnt += 1 #다음달에 받을 선물 수 카운트++
            elif giftsArr[i][j] == giftsArr[j][i]:#주고받은 수 같음
                if giveNum[i] - getNum[i] > giveNum[j] - getNum[j] : #두 친구의 선물지수 비교
                    cnt += 1 #다음달에 받을 선물 수 카운트++
        answer = max(answer, cnt) #max 갱신
    
    return answer

# 딕셔너리에 차례대로 이름과 점수를 집어넣는다.
# 반복문을 돌리면서 photo배열과 name을 비교해서 존재한다면, 점수를 합산한다.

def solution(name, yearning, photo):
    answer = []
    nameN = len(name)
    scoreDic = {name[i] : yearning[i] for i in range(nameN)}
    
    photoNum = len(photo) #2차원 배열 행 개수
    
    for i in range(photoNum): #행
        sum = 0
        for j in range(len(photo[i])): #열
            if photo[i][j] in name: #사진 속에 이름이 있는지 확인
                sum += scoreDic[photo[i][j]] # 점수 합산
        answer.append(sum)
        
    return answer

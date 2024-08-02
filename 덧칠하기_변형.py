def solution(k, requests):
    requestsNum = len(requests)
    cnt = 0
    answer = 0
    start = requests[0]


    for i in range(requestsNum):
        if i == 0 or start != requests[i]: 
            cnt = 1
        else:
            cnt += 1  # 같은 날짜의 요청일 경우 증가
        if cnt <= k:
            answer += 1 
        start = requests[i]  # start를 현재 날짜로 업데이트

    print(answer)


def main():
    k = 2
    requests = [1,2,2,2,3,3,4,4,4,4,5]

    solution(k, requests)

main()﻿​

def solution(k, score):
    answer = []
    arr = []
    
    for i in range(len(score)):
            arr.append(score[i])
            arr.sort(reverse = True)
            
            if i < k :
                answer.append(arr[i])
            else :
                answer.append(arr[k-1])
            
    return answer

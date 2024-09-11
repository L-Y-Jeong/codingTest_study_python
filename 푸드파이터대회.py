def solution(food):
    arr = []
    
    for i in range(1, len(food)):
        cnt = food[i] // 2
        arr.extend([str(i) * cnt])
        
    arr.append('0')
    
    arr.extend(reversed(arr[:-1]))
        
    return ''.join(arr)

def solution(n):
    arr = ['4','1','2']
    answer = []
    while n:
        if n%3 == 0:
            answer.append(arr[0])
            n-=1
        else:
            answer.append(arr[n%3])
        n//=3
        
    return ''.join(answer[::-1])
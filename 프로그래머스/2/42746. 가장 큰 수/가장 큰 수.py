def solution(numbers):
    answer = ''
    numbers = [str(st) for st in numbers]
    numbers.sort(key=lambda x: x*3,reverse = True) #자릿수대로 정렬
            
    answer = ''.join(numbers)
    return str(int(answer))
    
    
    
    
    # return answer
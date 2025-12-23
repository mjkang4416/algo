import itertools

def solution(word):
    answer = 0
    arr = ['A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(5):
        for alph in itertools.product(arr,repeat=i+1):
            result.append(''.join(alph))
    result.sort()
        
    return result.index(word)+1
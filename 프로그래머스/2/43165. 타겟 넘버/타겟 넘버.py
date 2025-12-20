import itertools 
import math

answer = 0

def dfs(numbers,target,current,idx):
    global answer
    
    if idx == len(numbers):
        if current == target:
            answer +=1
        return 
    
    dfs(numbers,target,current+numbers[idx],idx+1)
    dfs(numbers,target,current-numbers[idx],idx+1)
        
        
def solution(numbers, target):
    global answer
    dfs(numbers,target,0,0)
    return answer
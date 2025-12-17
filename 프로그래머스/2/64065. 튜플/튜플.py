
from collections import *

def solution(s):
    answer = []
    arr= s.replace("{","").replace("}","").split(",")
    result = Counter(arr).most_common() #숫자 빈도수 대로 dict
    answer = [ int(i[0]) for i in result]
    return answer
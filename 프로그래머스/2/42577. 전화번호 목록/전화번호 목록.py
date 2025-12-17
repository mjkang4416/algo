#한 번호가 다른 번호의 접두어
#어떤 번호가 다른번호의 접두어 -> false 아니면 true
#루프 두번 불가
#1이상 
#중복번호 들어있지 않음
#더 큰애가 작은애로 들어갈 순 없음 

from collections import *

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return answer
import sys

input = sys.stdin.readline
from collections import deque

# 과일 2종류 이하로 사용
# 앞에서 a 개 뒤에서 b 개 빼서 2종류만 남김 => 총 n -(a+b) 개 있음
# 2개 종류 남긴 탕후루 중 과일 개수 가장 많은거

n = int(input())
arr = list(map(int, input().split()))
dic = {}
left = 0
answer = 0

for i in range(n):
    right = i  # 현제 과일 인덱스

    if arr[right] in dic:  # 현재 과일이 dic 에 있는지 확인하고 넣음
        dic[arr[right]] += 1
    else:
        dic[arr[right]] = 1

    while len(dic) > 2:  # 넣은게 2 이상되면 left로 빼면서 shift
        dic[arr[left]] -= 1
        if dic[arr[left]] == 0:
            dic.pop(arr[left])
        left+=1 #left 하나 증가 , 얘가 start 고 right 가 사실상 end 인듯
    answer = max(answer,(right - left + 1))

print(answer)

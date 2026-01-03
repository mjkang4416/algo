import sys
input = sys.stdin.readline
import heapq
#d-1 최솟값 삭제 , d 1 최댓값 삭제
#I n 삽입
#삭제시 동일 숫자는 둘중 하나만 삭제됨
#비어있으면 삭제 무시
#큐에 남은값중 최대, 최솟값 출력 , 없으면 엠티 출력

t = int(input())

for i in range(t):
    n = int(input())
    hq_a = [] #오름차순
    hq_d = [] #내림차순
    dic = {}
    for j in range(n):
        commend , num = input().rstrip().split()
        num = int(num)
        if commend == 'I':
            if num in dic: #상태 관리할 딕셔너리
                dic[num]+=1
            else:
                dic[num] = 1
            heapq.heappush(hq_a,num)
            heapq.heappush(hq_d,-num)
        elif commend == 'D':
            if len(dic): #딕셔너리에 값이 있으면
                if num == -1 :
                    while hq_a and (hq_a[0] not in dic or dic[hq_a[0]] <1): #삭제할 값이 dic 에 없거나 0인 경우
                        temp = heapq.heappop(hq_a) #heap 에서 pop
                        if temp in dic:
                            dic.pop(temp)
                    if hq_a:
                        dic[hq_a[0]]-=1 #삭제할 값이 있는 경우
                else:
                    while hq_d and (-hq_d[0] not in dic or dic[-hq_d[0]]<1):
                        temp = -heapq.heappop(hq_d)  # heap 에서 pop
                        if temp in dic:
                            dic.pop(temp)
                    if hq_d:
                        dic[-hq_d[0]] -= 1  # 삭제할 값이 있는 경우

    if len(dic) :
        valid_key = [k for k in dic.keys() if dic[k]>0]
        if valid_key:
            print(max(valid_key),min(valid_key))
        else:
            print("EMPTY")
    else:
        print("EMPTY")



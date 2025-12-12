from collections import deque

n = int(input())

for _ in range(n):
    num,point = map(int,input().split()) #문서 개수, 찾으려는애 인덱스
    qu = deque()
    result = 0
    arr = list(map(int,input().split())) #중요도

    for i in range(num):
        qu.append((i,arr[i])) #인덱스랑, 우선순위 넣음 , 찾으려는애 인덱스면 ok

    while qu:
        isBig_true = False
        for i in range(len(qu)):
            if  qu[0][1] < qu[i][1]: #지금거보다 큰게 있다면 rotate
                    qu.rotate(-1)
                    isBig_true = True #큰거 존재 표시
                    break
        if not isBig_true:
            #지금거보다 큰게 없으면 큐에서 빼기
            now_queue = qu.popleft()
            result+=1
            if now_queue[0] == point :
                break
    print(result)
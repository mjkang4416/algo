import sys
from collections import deque

input = sys.stdin.readline
import heapq
#d-1 최솟값 삭제 , d 1 최댓값 삭제
#I n 삽입
#삭제시 동일 숫자는 둘중 하나만 삭제됨
#비어있으면 삭제 무시
#큐에 남은값중 최대, 최솟값 출력 , 없으면 엠티 출력

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    q = deque()
    q.append((a,''))
    visited = [False] * 10001
    visited[a] = True
    com = ['D','S','L','R']
    while q:
        node = q.popleft()
        now, result = node[0], node[1]
        if now == b:
            print(result)
            break

        for j in com:
            if j == 'D':
                temp = (now * 2) % 10000
                if not visited[temp]:
                    visited[temp] = True
                    q.append((temp, result+'D'))
            elif j == 'S':
                temp = (now - 1) % 10000
                if not visited[temp]:
                    visited[temp] = True
                    q.append((temp, result+'S'))
            elif j == 'L':
                temp = now//1000 + (now % 1000) * 10
                if not visited[temp]:
                    visited[temp] = True
                    q.append((temp, result+'L'))
            elif j == 'R':
                temp = now//10 + (now%10) * 1000

                if not visited[temp]:
                    visited[temp] = True
                    q.append((temp, result+'R'))


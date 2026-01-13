import sys
import heapq
input = sys.stdin.readline

#서로다른 두 정점 사이 여러개의 간선이 존재할 수 도 있다.
#해당 정점으로의 최단 경로 출력


def dijkstra(k):
    heap = []
    heapq.heappush(heap,(0,k)) #가중치, 시작노드
    dp[k] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if dist > dp[now]: #들어온애가 현재 값보다 크면 갱신 필요 없음 (중복 now 일때 작은값)
            continue

        for i in arr[now]:
            if dist+i[1] < dp[i[0]]: #다음노드 해당 노드 거쳐서 가는게 나은지 구함
                dp[i[0]] = dist+i[1]
                heapq.heappush(heap,(dist+i[1],i[0])) #갱신한 거리, 이거 통해서 가는게 더 짧은 경우 찾기 위해


v,e = map(int,input().split())
k = int(input())
arr = [[] for _ in range(v+1)]
for i in range(e):
    a,b,p = map(int,input().split())
    arr[a].append((b,p))


dp = [float('inf') for _ in range(v+1)]
dijkstra(k)
for i in range(1,v+1):
    if dp[i] == float('inf'):
        print('INF')
    else:
        print(dp[i])

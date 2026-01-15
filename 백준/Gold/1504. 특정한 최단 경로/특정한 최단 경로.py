import sys
input = sys.stdin.readline
import heapq
n,e = map(int, input().split())
#1-n 까지 v1,v2 를 거쳐서 가는 최단거리
#임의의 주어진 정점은 반드시 통과 해야 함
#한번 이동한 정점, 간선 중복 이동 가능
INF = float('inf')

arr = [[] for _ in range(n+1)]
for i in range(e):
    a,b,c = map(int,input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

v1,v2 = map(int,input().split())
def dijkstra(node):
    q = []
    result = [INF for _ in range(n+1)]
    heapq.heappush(q,(0,node))
    result[node] =0 #자기 자신까지 가는건 0 처리
    while q:
        dist,now_node = heapq.heappop(q)

        if result[now_node] < dist:
            continue

        for new_node,new_dist in arr[now_node]:
            if new_dist+dist < result[new_node] :
                result[new_node] = new_dist+dist
                heapq.heappush(q,(new_dist+dist,new_node))
    return result

one_to_v1 = dijkstra(1)[v1]
v1_to_v2 = dijkstra(v1)[v2]
v2_to_n = dijkstra(v2)[n]

one_to_v2 = dijkstra(1)[v2]
v2_to_v1 = dijkstra(v2)[v1]
v1_to_n = dijkstra(v1)[n]

answer_first_v1 = one_to_v1+ v1_to_v2+ v2_to_n
answer_first_v2 = one_to_v2 + v2_to_v1 + v1_to_n

if answer_first_v1 ==INF or answer_first_v2==INF:
    print(-1)
else :
    print(min(answer_first_v1, answer_first_v2))
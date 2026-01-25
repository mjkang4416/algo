import sys
input = sys.stdin.readline


def bf():
    d = [2000000 for _ in range(n+1)] #각 노드까지 최단거리 저장하는 배열
    d[1] = 0 #어떤 노드를 출발점으로 해도 음수 사이클 감지 가능

    # N번 검사
    for i in range(n):
        for ar in arr: #모든 간선 검사
            start,goal,time = ar #1이랑 연결된 노드부터 검사
            if d[goal] > d[start] + time: #start 노드를 거쳐서 가는거보다 현재 목적지가 큰 경우
                d[goal] = d[start] + time #갱신
                # N번 시행시 갱신된다면, 음의 가중치 판단, 한바퀴 다 돌았는데 갱신됐으니까
                if i == n - 1:
                    return 'YES'
    return 'NO'

t = int(input())
for _ in range(t):
    n,m,w = map(int, input().split()) # n(노드),m(도로),w(웜홀) 개수
    arr = []
    for _ in range(m):
        a,b,t = map(int,input().split())
        arr.append((a,b,t))
        arr.append((b,a,t))
    for _ in range(w):
        a,b,t = map(int,input().split()) #시작지점, 도착지점, 줄어드는시간
        arr.append((a,b,-t))
    print(bf())
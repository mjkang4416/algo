#나무한줄 ->절단허가
#나도 M 미터 필요
#높이 h
#해당 줄 한번에 잘림
#높이보다 큰 나무만 잘림
#M 미터 가져가기 위한 높이 최댓값
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr =list(map(int,input().split()))

def binary_search(start,end):
    global m,n
    while start <= end:
        mid = (start+end)//2
        sum = 0
        for i in range(n):
            if arr[i]>mid:
                sum+= arr[i]-mid #mid 가 커질수록 조금남음

        if sum >= m: #sum 이 너무 큰 경우 mid 키워야
            start = mid+1
        else: #sum 이 너무 작은경우 mid 작게 만들어야
            end = mid-1
    print(end)
binary_search(1,max(arr))
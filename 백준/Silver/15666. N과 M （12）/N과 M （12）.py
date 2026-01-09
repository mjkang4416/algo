import itertools
import sys
input = sys.stdin.readline

#n 개중 m 개를 고른거
#중복 조합 가능
#고른 수열은 오른차순
n,m = map(int,input().split())
arr = set(map(int,input().split()))
result = []
arr = list(itertools.combinations_with_replacement(arr,m))

for i in arr:
    result.append(sorted(i))

for i in reversed(range(m)):
    result.sort(key=lambda x : x[i]) #뒤기준 정렬해야 앞이 같을때 유지 , 앞 기준 정렬하면 뒤가 같을때만 유지되고 다르면 바뀜

for i in result:
    print(*i)

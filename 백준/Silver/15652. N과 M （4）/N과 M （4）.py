import sys
import itertools
input = sys.stdin.readline

n,m =map(int,input().split())
arr = [i for i in range(1,n+1)]
result = list(itertools.combinations_with_replacement(arr,m))

result.sort(key=lambda x : x[0])
for i in result:
    for j in i:
        print(j,end=" ")
    print()
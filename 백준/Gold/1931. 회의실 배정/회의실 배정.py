import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    s,e = map(int,input().split())
    arr.append([s,e])

arr.sort(key=lambda x : (x[1],x[0])) #끝나는 시간이 짧은 순으로 정렬

result = 1
end = arr[0][1]
for i in range(1,n):
    if end <= arr[i][0] : #끝나는 애보다 새로 들어오는 시작점이 크거나 같으면
        end = arr[i][1]
        result += 1
print(result)
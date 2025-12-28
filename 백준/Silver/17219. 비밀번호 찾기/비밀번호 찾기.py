import sys
input = sys.stdin.readline

n,m = map(int,input().split()) #저장된 사이트 주소수, 비번 찾으려는 사이트 주소 수
dic = {}
for i in range(n):
    a,b = input().rstrip().split()
    dic[a] = b

for j in range(m):
    st = input().rstrip()
    print(dic[st])

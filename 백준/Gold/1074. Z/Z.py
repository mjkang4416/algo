import sys
input = sys.stdin.readline

n,r,c = map(int,input().split()) #r행 c 열 을 몇번째로 방문했는지
n = 2**n
# 4분할이니까 4씩 분할해서
def z(r,c,n,result):
    n//=2
    if r<n and c<n: #1사분면에 있는 경우
        if n==1:
            print(result)
            exit(0)
        z(r,c,n,result)
    elif r<n and c>=n: #2사분면에 있는 경우
        if n == 1:
            print(result+1)
            exit(0)
        z(r, c-n, n, result+n**2) #1사분면 지나감으로 n**2
    elif r>=n and c<n: #3사분면에 있는 경우
        if n == 1:
            print(result+2)
            exit(0)
        z(r-n, c, n, result+n**2*2)
    elif r>=n and c>=n: #4사분면에 있는 경우
        if n == 1:
            print(result+3)
            exit(0)
        z(r-n, c-n, n, result + n ** 2 * 3)


z(r,c,n,0)

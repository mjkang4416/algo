import sys

input = sys.stdin.readline

#a를 b번 곱한수, 너무 커지면 안되니까 c로 나눠가면서 곱하자

a,b,c = map(int,input().split())

def multiple(num):
    if num ==1:
        return a % c
    if num%2 ==0:
        return (multiple((num//2))**2)%c
    else:
        return (multiple((num // 2))**2) * a % c
print(multiple(b))
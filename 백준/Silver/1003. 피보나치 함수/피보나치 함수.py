import sys
from collections import deque
input = sys.stdin.readline


t = int(input())
arr = []
for _ in range(t):
    n = int(input())
    one = [0]*41
    zero = [0]*41
    one[0],one[1] = 0,1
    zero[0],zero[1] = 1,0

    for i in range(2,n+1):
        one[i] = one[i-1]+one[i-2]
        zero[i] = zero[i-1] + zero[i-2]
    print(zero[n],one[n])
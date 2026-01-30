import sys

input = sys.stdin.readline

n = int(input())
tree = [list(input().rstrip().replace(' ','')) for _ in range(n)]
map = {}
for i in range(n):
    if tree[i][0]!=' ':
        map[tree[i][0]] = [tree[i][1],tree[i][2]]


# 전위 루/왼/오
def preorder(now):
    if now !='.':
        print(now,end="")
    if map[now][0] != '.':
        preorder(map[now][0])
    if map[now][1] != '.':
        preorder(map[now][1])

# 중위 왼/루/오
def inorder(now):
    if map[now][0] != '.':
        inorder(map[now][0])
    if now != '.':
        print(now, end="")
    if map[now][1] != '.':
        inorder(map[now][1])
# 후위
def last_order(now):
    if map[now][0] != '.':
        last_order(map[now][0])
    if map[now][1] != '.':
        last_order(map[now][1])
    if now != '.':
        print(now,end="")

preorder('A')
print()
inorder('A')
print()
last_order('A')
import sys
input = sys.stdin.readline

def preorder(root):
    if root != '.':
        print(root, end='')
        if tree[root][0] != '.':  # 왼쪽이 있으면
            preorder(tree[root][0])
        if tree[root][1] != '.':  # 오른쪽이 있으면
            preorder(tree[root][1])  # 오른쪽으로


def inorder(root):
    if root != '.':
        if tree[root][0] != '.':  # 왼쪽이 있으면
            inorder(tree[root][0])
        print(root, end='')
        if tree[root][1] != '.':  # 오른쪽이 있으면
            inorder(tree[root][1])  # 오른쪽으로


def postorder(root):
    if root != '.':
        if tree[root][0] != '.':  # 왼쪽이 있으면
            postorder(tree[root][0])
        if tree[root][1] != '.': #오른쪽이 있으면
            postorder(tree[root][1]) #오른쪽으로
        print(root,end='')


n = int(input())
tree = dict()
for i in range(n):
    root,left,right =input().rstrip().split()
    tree[root] = [left,right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
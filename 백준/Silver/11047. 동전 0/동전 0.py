#거슬러줄 돈 개수, 거슬러줄 돈 
n , k = map(int,input().split())

allList=[]

for _ in range(n):
    allList.append(int(input()))

# 거스름돈 단위 오름차순으로 sorting
allList.sort(reverse=True)

count = 0

for i in allList :
    if k >= i:
        count += k//i
        k %= i
    
print(count)
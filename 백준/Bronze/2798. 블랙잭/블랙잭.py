n, m = map(int, input().split())

nList = list(map(int,input().split()))

num = 0 
maxNum = 0

for i in range(len(nList)-2):
    for j in range(i+1,len(nList)-1):
        for k in range(j+1,len(nList)):
            num = nList[i]+nList[j]+nList[k]
            if num <= m and num > maxNum:
                maxNum = num
                
print(maxNum)
    
    
    
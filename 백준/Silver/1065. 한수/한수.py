n = int(input())
count = 0
#1 부터 99 까지 즉 2자리수까지는 무조건 한수이다. 

for i in range(1,n+1):
    if i <100:
        count += 1
    
    else:
        num = list(map(int,str(i)))
        if num[1]-num[0] == num[2]-num[1]:
            count +=1

print(count)
n = int(input())
st = []
num = 0
for _ in range(n):
    st.append(input())

for i in range(len(st)):
    found = False
    for j in range(len(st[i])-1):
        for k in range(j+1,len(st[i])):
            if(st[i][j]==st[i][k] and st[i][k]!=st[i][j+1]):
               found = True
               break
        if found == True : 
            break
    if found != True:
        num+=1 
print(num)
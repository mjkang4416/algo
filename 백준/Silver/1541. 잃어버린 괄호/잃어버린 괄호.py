exp = input().split('-') # - 기준으로 나눠서 exp list 에 저장
num = []

for i in exp:
    sum = 0
    temp = i.split('+') # 나눠진 exp 리스트를 다시 + 기준으로 split
    for j in temp: # + 를 나누기 위해 임시로 만든 list +할 요소들이 들어있음
        sum += int(j) #+ 연산 수행
    num.append(sum) # 더해서 들어간거 들어있음 이제 - 만 하면 됌
    
n = num[0] #이제 뺄셈만 할거임, 첫번째 값부터 빼야함으로 num[0]을 넣어줌

for i in range(1,len(num)):
    n -= num[i]


print(n)    
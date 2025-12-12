n,m = map(int,input().split()) # 가로,세로

arr = [list(map(int,input())) for _ in range(n)] #배열

min_num = min(n,m)
result = 1

for i in range(n-1):
    for j in range(m-1): # 완탐 , 어짜피 넓이가 2부터 시작임으로
        for num in range(1,min_num):
            if i+num >= n or j+num >= m : #가로 세로 범위 벗어날 경우
                continue
            else :
                # 꼭짓점 같은지 체크
                if arr[i][j] == arr[i+num][j] == arr[i][j+num] == arr[i+num][j+num]:
                    result = max(result,((num+1)*(num+1)))

print(result)
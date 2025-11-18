import copy

n,m,x,y,k= map(int,input().split()) # 주사위를 놓은 곳의 좌표 x, y, 명령개수 k

arr = [list(map(int,input().split())) for _ in range(n) ]

menual = list(map(int,input().split())) # 서,동 2,1 북,남 3,4

dic = [[0]*3 for _ in range(4)] #주사위 배열 

def suitMen(x,y,dic): #실재 명령 수행 

    #지도 바닥면이 0 인 경우
    if arr[x][y] == 0:
        arr[x][y] = dic[3][1]
    #아닌경우 
    else :
        dic[3][1] = arr[x][y]
        arr[x][y] = 0

    print(dic[1][1])



for men in menual :
    clonDic = copy.deepcopy(dic) #복사

    if men == 1 : #동
        #이동 가능한시 검사 불가하면 해당 명령 무시 
        if y+1 <m :
            y+=1
            #주사위 굴렸을때 모습
            clonDic[1][0] = dic[3][1] 
            clonDic[1][1] = dic[1][0]
            clonDic[3][1] = dic[1][2]
            clonDic[1][2] = dic[1][1]

            dic = clonDic # 바꾼 배열을 진짜 배열로 만들어줌 

            suitMen(x,y,dic) #주사위 위치와, 바뀐 주사윗값 전달
        
    
    elif men == 2 : #서
        #이동 가능한시 검사 불가하면 해당 명령 무시 
        if y-1 >= 0 :
            y-= 1
            #주사위 굴렸을때 모습
            clonDic[1][0] = dic[1][1] 
            clonDic[1][1] = dic[1][2]
            clonDic[3][1] = dic[1][0]
            clonDic[1][2] = dic[3][1]

            dic = clonDic # 바꾼 배열을 진짜 배열로 만들어줌 

            suitMen(x,y,dic) #주사위 위치와, 바뀐 주사윗값 전달

    
    elif men == 3 : #북
        #이동 가능한시 검사 불가하면 해당 명령 무시 
        if x-1 >=0 :
            x-=1
            #주사위 굴렸을때 모습
            clonDic[3][1] = dic[0][1]
            for i in range(3) :
                clonDic[i][1] = dic[i+1][1]

            dic = clonDic # 바꾼 배열을 진짜 배열로 만들어줌 

            suitMen(x,y,dic) #주사위 위치와, 바뀐 주사윗값 전달
        

    elif men == 4 : #남
        #이동 가능한시 검사 불가하면 해당 명령 무시 
        if x+1 <n :
            x+=1
            #주사위 굴렸을때 모습
            clonDic[0][1] = dic[3][1]
            for i in range(1,4) :
                clonDic[i][1] = dic[i-1][1]

            dic = clonDic # 바꾼 배열을 진짜 배열로 만들어줌 

            suitMen(x,y,dic) #주사위 위치와, 바뀐 주사윗값 전달
       

    
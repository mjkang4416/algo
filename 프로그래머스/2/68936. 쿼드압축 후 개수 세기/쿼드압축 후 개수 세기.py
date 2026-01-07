one_cnt = 0
zero_cnt = 0
def solution(arr):
    answer = []
    #s 내부에 있는수가 같은거면 s 해당수로 압축 
    #아니면 균일정사각형으로 쪼갠뒤에 같은 방식 
    #최종적으로 남는 0의 개수와 1의 개수 
    n = len(arr)

    def bfs(x,y,n):
        global one_cnt
        global zero_cnt
        
        one_bool = any(1 in i[y:y+n] for i in arr[x:x+n])
        zero_bool = any(0 in i[y:y+n] for i in arr[x:x+n])
        
        if one_bool and zero_bool : #해당 변에 둘다 존재하면 
            n=n//2
            bfs(x,y,n)
            bfs(x,y+n,n)
            bfs(x+n,y,n)
            bfs(x+n,y+n,n)
            return
        
        if one_bool and not zero_bool:
            one_cnt +=1
            return
                
        if not one_bool and zero_bool:
            zero_cnt +=1
            return
        
        


    bfs(0,0,n)
    result = [zero_cnt,one_cnt] 
    return result
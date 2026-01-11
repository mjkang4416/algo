def solution(book_time):
    answer = 1
    result =[]
    room = []
    for i,j in book_time:
        start_h,start_m = map(int,i.split(':'))
        end_h,end_m = map(int,j.split(':'))
        
        result.append([start_h*60+start_m,end_h*60+end_m+10])
        
    result.sort(key = lambda x:x[0])
    
    room.append([result[0][1]])
    
    
    for i in range(1,len(result)):
        is_new_room = False
        start = result[i][0]
        
        for j in range(len(room)):
            end = room[j][0]
            if end  <= start:
                room[j][0]= result[i][1] #바꿔주기만 하면 됨 
                is_new_room = True
                break
        if not is_new_room:
            room.append([result[i][1]]) #end 값을 넣어줌
    return len(room)
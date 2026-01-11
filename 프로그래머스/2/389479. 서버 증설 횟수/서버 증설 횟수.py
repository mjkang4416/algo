def solution(players, m, k):
    #m 명 이상이면 1대 추가 
    #m 미만이면 증설 필요없음 
    #한번 증할한애는 k 시간동안 운영 
    #서버 최소 몇번 증설해야 하는지 
    cnt = 0
    plus_arr = [0 for _ in range(len(players)+1)]

    for i in range(len(players)):
        if players[i] >=m:
            if plus_arr[i] < players[i]//m:
                remain = (players[i]//m - plus_arr[i])
                for j in range(k): #n초만큼 증설 유지
                    if i+j <= len(players):
                        plus_arr[i+j] += remain
                cnt += remain
    # return plus_arr

    return cnt
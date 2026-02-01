from itertools import product
def solution(users, emoticons):
    #임플많고, 구매비용 최대가 되는 가입수,매출액 reutrn 
    #10 20 30 40 중 하나 할인률
    n = len(users)
    m = len(emoticons)
    arr= [10,20,30,40]
    result = []
    # 임플 최대
    # 30,40 중 하나 그럼 살수는 있되, 젤 작게 할인해야 임티플 하겠지 
    hall_percent_list = list(product(arr,repeat=m))
    for percent in hall_percent_list:
        temp_emption = [0]*m
        imo = 0
        for i in range(len(emoticons)): 
            temp_emption[i] = [emoticons[i]*(100-percent[i])//100,percent[i]] #할인된 가격 list 
        
        per_imo = 0
        per_user_price = 0
        for user in users: #유저마다 할인가 확인 -> 구매 
            user_price = 0
            user_imo =0
            for imo in temp_emption: 
                if user[0]<=imo[1]: #할인률이 더클때 구매가 더함
                    user_price+=imo[0]
            if user_price >= user[1]: #임계치 넘어가면 이모지 
                user_imo+=1
                user_price = 0
            per_imo+=user_imo
            per_user_price+=user_price
        result.append([per_imo,per_user_price])
        
    result.sort(key=lambda x: (-x[0],-x[1]))
    return result[0]
                
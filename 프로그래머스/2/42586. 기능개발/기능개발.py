# 개발 완료 순서 다 다름
# 뒷기능은 앞 기능 배포될때 함께 배포
# progresses 완료 %  , 뒤에게 앞에거보다 빨라도 앞에거에 의존성 
# speeds 각 개발 속도 적힘
# 각 배포마다 몇개의 기능 배포 ? 
# 배포는 하루에 한번, 하루의 끝에 
from collections import deque
from collections import Counter

def solution(progresses, speeds):
    answer = deque()
    for i in range(len(progresses)):
        result = 0 #작업 더 해야하는 날짜 
        if (100-progresses[i])%speeds[i] == 0: #나누어 떨어지는 경우 
            result = (100-progresses[i])//speeds[i]
        else : #나누어 떨어지지 않는 경우 
            result = ((100-progresses[i])//speeds[i])+1
        answer.append(result) #진도별로 몇일 걸리는지 기록
    
    for i in range(1,len(answer)): # 우선순위 안맞는 경우 숫자 바꿔줌 
        #뒤에 있는애가 앞에 있는 애보다 작은 경우 
        if answer[i] < answer[i-1] :
            answer[i] = answer[i-1]
            
    cnt = Counter(answer) #각 숫자가 몇개 있는지
    re = []
    for i in cnt.values() :
        re.append(i)
            
    return re
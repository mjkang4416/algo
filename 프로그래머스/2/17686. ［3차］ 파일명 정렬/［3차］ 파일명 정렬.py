#영문/대소/숫자/공백/./- 로 이루어짐
#영문자 시작, 숫자 하나이상 포함 
#head : 문자, 1글자 이상 number: 앞쪽 0 가능 0~99999 tail: 암거나 가능 
#파일명 3부분으로 나눈뒤 기준따라 정렬
#대소문자 구분안함 
#head 기준 사전순 정렬 
#head 가 같으면 number 로 정렬 숫자앞 0 무시
#두개다 같으면 원래 순서 유지 
def solution(files):
    arr = {}
    idx = 0
    for i in files: #head,number 로 나누고 0 자름 
        st = ''
        num = ''
        point = 0
        for j in range(len(i)):
            if not i[j].isdigit():
                st+=i[j]
                point+=1
            elif i[j].isdigit():
                break
        for k in range(point,len(i)):
            if i[k].isdigit():
                num+=i[k]
            elif not i[k].isdigit():
                break
        arr[idx]=(st.lower(),int(num))
        idx+=1
        
    sorted_dic = sorted(arr.items(),key=lambda x:(x[1][0],x[1][1]))
    answer =[]
    for i in sorted_dic:
        answer.append(files[i[0]])
    return answer

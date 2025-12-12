import collections

arr = list(input()) #문자 받아서 리스트에 하나하나 넣기

arr.sort() #알파벳 순으로 sort
count_dict = collections.Counter(arr) #이러면 같은 단어 딕셔너리 형태로 세 준다고 한다.. ex) {'A': 3, 'B': 2}
cnt = 0
hol = ""
for alpha,num in count_dict.items() : # 홀수 찾기
    if num % 2 != 0: #홀수라면
        hol = alpha
        cnt +=1
    if cnt > 1 :
        print("I'm Sorry Hansoo")
        exit()

result =""
for alpha,num in count_dict.items(): #짝수 개수로 자르기
    result+= ((num//2)*alpha)

print(result + hol + result[::-1])
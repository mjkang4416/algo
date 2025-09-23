## **문제**

데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.

간단한 예로 "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다. "어피치"는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.

예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.

다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만, 3개 단위로 자른다면 "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.

압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

### **제한사항**

> s의 길이는 1 이상 1,000 이하입니다.s는 알파벳 소문자로만 이루어져 있습니다.
> 

### **입출력 예**

> sresult"aabbaccc"7"ababcdcdababcdcd"9"abcabcdede"8"abcabcabcabcdededededede"14"xababcdcdababcdcd"17
> 

### **입출력 예 설명**

- 입출력 예 #1

문자열을 1개 단위로 잘라 압축했을 때 가장 짧습니다.

- 입출력 예 #2

문자열을 8개 단위로 잘라 압축했을 때 가장 짧습니다.

- 입출력 예 #3

문자열을 3개 단위로 잘라 압축했을 때 가장 짧습니다.

- 입출력 예 #4

문자열을 2개 단위로 자르면 "abcabcabcabc6de" 가 됩니다.

문자열을 3개 단위로 자르면 "4abcdededededede" 가 됩니다.

문자열을 4개 단위로 자르면 "abcabcabcabc3dede" 가 됩니다.

문자열을 6개 단위로 자를 경우 "2abcabc2dedede"가 되며, 이때의 길이가 14로 가장 짧습니다.

- 입출력 예 #5

문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.

따라서 주어진 문자열을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능 합니다.

이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다.

---

## 소감

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(String s) {
        int answer = 0;
        int INF = (int)1e9; 
        int bundleResult = INF; 
        int bundle =0; //원래 list 에서 나눠 떨어지는수 
        int remain = 0; //남은거
        
        ArrayList<Character> st = new ArrayList<>(); 
        
        for(int i =0; i<s.length(); i++){
            st.add(s.charAt(i));
        }
        
        for(int i =1; i<=st.size()/2; i++){ //각 단위 
            ArrayList<ArrayList<Character>> arr = 
                new ArrayList<ArrayList<Character>>(); 
            bundle = st.size()/i;
            remain = st.size()%i;
            
            for(int j=0; j<bundle; j++){
                arr.add(new ArrayList<Character>());
            }
             int index = 0; 
            
            for(int q=0; q<bundle; q++){  // 문자열 arr 에 단위씩 잘라서 할당 
                //i 가 단위니까 
                List<Character> sub = st.subList(index,index+i); //sub 반환이 list래.. 
                index+=i; 
            }
            
            ArrayList<Character> result = new ArrayList<>(); //결과 배열 
            int equalNum = 1; 
            for(int k=0; k<bundle-1; k++){
                // 두개 list 같은경우 equalNum 증가 
                if(arr.get(k).equals(arr.get(k+1))){ 
                    equalNum++; 
                }
                else { //두개 list 다른경우 
                    Character ct = (char)equalNum; 
                    result.add(ct); //숫자 
                    for (Character c : arr.get(k)) {
                        result.add(c);
                    }
                    
                    equalNum = 1; // 초기화 
                }
                   
                if(k+1 == bundle-1){ //마지막 list 는 같던 다르던 무조건 삽입 
                    Character ct = (char)equalNum; 
                    result.add(ct); //숫자 
                    for (Character c : arr.get(k)) {
                        result.add(c);
                    }
                }
            }
            
            
            //나머지 단위 x 배열 삽입 
            for(Character c : st.subList(bundle*i,s.length())){
                result.add(c); 
            }
            
                       
            if(result.size() < bundleResult){ //이것도  answer = Math.min(answer, result.length()); 이런식으로 줄이자.
                bundleResult = result.size(); 
                answer = bundleResult; 
            }
        }
        return answer;
    }
}
```

처음 잘못 풀었을때 보다시피 코드가 길다. 

다른사람들 풀이를 보니 답을 도출하는 알고리즘 자체는 똑같은데 내가 list sub 쪽 구현을 어떻게 해야할지 고민

하다가 list 전체를 ArrayList 에 넣고 빼고 난리를 치다 보니 .. 복잡해져서 코드 중간중간 오류가 생겼지 않을까 

싶다 (너무 복잡한 문제는 변수 쓰면서도 이변순지 저변순지 헷갈린다 .. ) 즉 구현에서 문제가 생겼다는 말! 

나머지는 count 를 써서 횟수 추가, 다른 배열이 생기면 건너뛰고 마지막 배열을 넣어주는 아이디어 까지 똑같았다. 

그래도 나름 답안에 근접해서 열심히 공부한 보람이 있었다고 .. 

```java
class Solution {
    public int solution(String s) {
        int answer = s.length();
        int count = 1;
        for(int i=1; i<=s.length()/2; i++){
            StringBuilder result = new StringBuilder();
            String base = s.substring(0, i);
            for(int j=i; j<=s.length(); j+=i){
                // 이미 base에서 하나는 count 했음 (j=i)
                int endIdx = Math.min(j + i, s.length());   // 인덱스는 길이를 넘을수 없음
                String compare = s.substring(j, endIdx);
                if(base.equals(compare)){
                    count++;
                } else {
                    if(count >= 2){
                        result.append(count);
                    }
                    result.append(base);
                    base = compare;     // 마지막 인덱스일때 한번 더 더해야함 (딱 안떨어지는 경우 있음)
                    count = 1;
                }
            }
            result.append(base);    // 마지막 문자 붙이기
            answer = Math.min(answer, result.length());
        }
        return answer;
    }
}
```

정답 코드이다. 풀이과정은 똑같아서 코드이해 → 부족했던 점 중심으로 살펴보려 한다. (굳이 받아쓰기 하지는 않았다.) 

나의문제점

- **String.substring(startIndex, endIndex)** 일단 이게 있는줄 몰랐다 .. **검색을 많이 하더라도 활용할 수 있는 함수좀 찾아보자**. 이거 안되는 줄 알고 list 를 통채로 넣고 ArrayList 만들고 난리를 쳤다.
- **Stringbuilder 를 사용** 할 수도 있다. (String 과 달리 가변 객체 내부 버퍼(buffer)를 사용해 문자열을 바꿀 수 있다. ) 이게 있으면 따로 결과 list 또한 안 만들어도 될 듯 하다. ~~점점 코테 공부인지 자바 공부인지 모르겠다…~~
- String base = s.substring(0, i); 베이스를 두는 방법을 떠올리지 못했다. 나는 단위수로 나누고 난 후 단위수만큼 비교를 하고 남은걸 add 해 주려 했는데 이분은 base 를 두고 base 를 계속 다음에 잘린 묶음(얘도 변수처리 해 주었다.) 과 비교하며 base 와 다른게 생기면 해당 묶음으로 base 를 갱신 해 나간다. (이때 out of bound 방지를 위해 min 함수 처리고 해 주었다. 이 두부분을 생각하지 못해 애를 먹었었는데 

나의 경우 (arr.get(k).equals(arr.get(k+1)) 이런식으로 k 번째 묶음과 다음 묶음 list 를 비교하려 했다. 
이렇게 하니 k+2 까지 k 항과 같을때 나는 k+1 항과 k+2 항을 비교하고 있기 때문에 처음 비교했던 기준노드 k 항을 넣기가 애매해 졌다. 그래서 마지막 k+2 항을 넣고 cout 만 ++ 해 주었는데 기준 **묶음을 변수로 잡고 
갱신** 해 나가는게 더 직관적인 방법인 것 같다.
- **대소 비교시 Math.min 함수 쓰는 습관을 들이자**. 코드 수 줄어든다.
- int endIdx = Math.min(j + i, s.length());   // 인덱스는 길이를 넘을수 없음
                String compare = s.substring(j, endIdx);
에서 나는 OutOfBound 때문에 bundle(나누어 떨어지는수) 과 remain(나머지) 로 넣을 묶음을 분리했었다. 
이렇게 **outOfBound 됐을때를 대비해 넘으면 s.length() 를 선택하게** 해 놓으니 알고리즘이 훨씬 간단 해 졌다.

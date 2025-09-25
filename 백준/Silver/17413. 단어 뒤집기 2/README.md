# [Silver III] 단어 뒤집기 2 - 17413 

[문제 링크](https://www.acmicpc.net/problem/17413) 

### 성능 요약

메모리: 22760 KB, 시간: 228 ms

### 분류

구현, 자료 구조, 문자열, 스택

### 제출 일자

2025년 9월 25일 21:19:09

### 문제 설명

<p>문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 한다.</p>

<p>먼저, 문자열 S는 아래와과 같은 규칙을 지킨다.</p>

<ol>
	<li>알파벳 소문자('<code>a</code>'-'<code>z</code>'), 숫자('<code>0</code>'-'<code>9</code>'), 공백('<code> </code>'), 특수 문자('<code><</code>', '<code>></code>')로만 이루어져 있다.</li>
	<li>문자열의 시작과 끝은 공백이 아니다.</li>
	<li>'<code><</code>'와 '<code>></code>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<code><</code>'이 먼저 등장한다. 또, 두 문자의 개수는 같다.</li>
</ol>

<p>태그는 '<code><</code>'로 시작해서 '<code>></code>'로 끝나는 길이가 3 이상인 부분 문자열이고, '<code><</code>'와 '<code>></code>' 사이에는 알파벳 소문자와 공백만 있다. 단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 연속하는 두 단어는 공백 하나로 구분한다. 태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.</p>

### 입력 

 <p>첫째 줄에 문자열 S가 주어진다. S의 길이는 100,000 이하이다.</p>

### 출력 

 <p>첫째 줄에 문자열 S의 단어를 뒤집어서 출력한다.</p>

# 소감

```java
import java.util.ArrayList;
import java.util.Scanner;

public class WordFlip2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String st = sc.nextLine();

        ArrayList<ArrayList<Character>> arr = new ArrayList<ArrayList<Character>>();

        int space =0;

        // 문자열 슬라이싱 -> arrList 에 넣어줌
        for(int i =0; i<st.length(); i++){
            if(st.charAt(i) == '<'){ //일 경우 >가 올떄가지 스페이스가 있어도 넘어감\
                ArrayList<Character> ch = new ArrayList<Character>();
                while (true){
                    ch.add(st.charAt(i));
                    if(st.charAt(i) == '>'){
                        break;
                    }
                    i++;
                }
                arr.add(ch);
            }
            if(st.charAt(i) == ' ' || i == st.length()-1){ //공백 올 경우 잘라서 list 에 저장
                String s;
                if(i==st.length()-1){
                    s = st.substring(space,i+1);
                }
                else{
                    s = st.substring(space,i);
                }
                space = i;
                ArrayList<Character> ch = new ArrayList<Character>();
                for(int j =0; j<s.length(); j++){
                    ch.add((Character)s.charAt(j));
                }
                arr.add(ch);
            }
        }

        //슬라이싱 한 문자열 뒤바꾸고 -> result 에 넣어줌
        for(int i =0; i<arr.size(); i++){
            Character[] result = new Character[arr.get(i).size()];
            for(int j =0; j<arr.get(i).size(); j++){
                    // arr 0 묶음의 j 번째가 < 일떄
                    if(arr.get(i).get(j) == '<') {//'>' 나올때까지 그냥 넣음
                        while(true){
                            result[j] = arr.get(i).get(j);
                            j++;
                            if(arr.get(i).get(j) == '>'){
                                result[j] = arr.get(i).get(j);
                                break;
                            }
                        }
                    }
                    else{ //< 가 아니라 숫자나 문자인 경우
                        ArrayList<Character> swap = new ArrayList<>(); //< 전이나, 마지막까지 담을 list
                        int firstIndex = j; //> 다음 인덱스 저장
                        while (true) {
                            if(arr.get(i).get(j) =='<' || j==arr.get(i).size()-1){
                                if(j==arr.get(i).size()-1){
                                    swap.add(arr.get(i).get(j));
                                }
                                swapList(swap,firstIndex,result);

                                break;
                            }
                            swap.add(arr.get(i).get(j));
                            j++;
                        }
                    }
            }
            for(int q = 0; q<result.length; q++){
                System.out.print(result[q]);
            }
            System.out.print(" ");
        }
    }
    public static void swapList(ArrayList<Character> arr, int firstIndex,Character[] result){ //스왑해서 result 에 넣기
        int lastPoint = arr.size()-1;
        for(int i =0; i<arr.size()/2; i++){ //swap
            Character existing = arr.get(i);
            arr.set(i,arr.get(lastPoint));
            arr.set(lastPoint,existing);
            lastPoint--;
        }
        for (Character character : arr) {
            result[firstIndex] = character;
            firstIndex++;
        }
    }
}

```

와우 길죠 ? 구현이라고 스택 쓰는걸 생각을 못했다 .. . 구현도 자료구조 생각하면서 하기 .. 문자열 괄호 할때 스택

에 넣어서 쓰는거 했으면서 왜 생각을 못했는지 모르겠다. 구현도 쌩구현 하려 하지말고, 무슨 자료구조, 알고리즘 

쓰면 효율적으로 구현될지 생각해면서 하자 .. 아니면 코드량 너무 많아진다 .. 심지어 예외가 너무 많아서 저렇게 하

면 안돌아감. 

```java
package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String s = br.readLine();
        Stack<Character> stack = new Stack<>();

        boolean check = false;

        for (int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '<'){ //< 만난 순간 그전까지 읽었던거 뽑기
                check = true;
                while(!stack.empty()){
                    sb.append(stack.pop());
                }
                sb.append(s.charAt(i));
            }

            else if(s.charAt(i) == '>'){ //> 만나면 괄호 전에 있었던거 다 넣기 
                check = false;
                sb.append(s.charAt(i));
            }

            else if(check){ // < 다음 인 경우 괄호 열린거 걍 넣기 
                sb.append(s.charAt(i));
            }

            else if(!check){ //< > 바깥이고
                if(s.charAt(i) == ' '){ //공백이면 공백 전거 다 뒤집어서 뽑기
                    while(!stack.empty()){
                        sb.append(stack.pop());
                    }
                    sb.append(s.charAt(i));
                } //공백이 아닌 경우
                else {
                    stack.push(s.charAt(i)); //넣기 
                } 
            }
        }

        while(!stack.empty()){
            sb.append(stack.pop());
        }

        System.out.println(sb.toString());
    }

}
```

계속 할 수 있을 것 같은데 .. 하면서 뻐팅기다가 이 이상 보는건 시간낭비 같고 , 이렇게 푸는건 백퍼 틀린 풀이란

생각이 들어서 ~~(코드가 너무 길었다.~~ ) 그냥 정답을 보기로. 

1. 구현 문제도 자료구조나 알고리즘 뭐 쓸지 생각하자.. 쌩 구현 하지 않기로 해~ 
2. ArrayList 로 문자열 처리할 생각좀 그마 ㄴ… 너무 복잡해서 그걸로 절대 안되니까 좀 포기해
3. 다시 ArryList 가 등장한 이유 subString 은 기억했는데 StringBuilder 를 까먹었다 !!!!! 인간의 기억력이란 .. 그래서 결국 동적공간 할당이 안된다고 생각해서 다시 등장한 것
4. 이 구현이 안되는거 같으면 그냥 빨리 답 보기 …. 교훈 얻고  새로 푸는게 낫다. 
5. 문자열은 왠만하면 스택 쓰자 . 괄호넣기도 스택이었는데 왜 생각을 못했는지.

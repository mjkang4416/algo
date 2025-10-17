import java.util.*;

class Solution {
    static String result=""; 
    static String p;
    static String answer = "";
    static String u = "", v = "";
    
    static Deque<Character> stack = new ArrayDeque<>();
    
    public String solution(String p) {
        
        //문자열 빈경우 빈 문자열 반환
        if(p.isEmpty()){
           return p;
        }
        else {
            //비지 않은 경우
             answer = dfs(p);
             return answer;
            }
        
    }
    
    public String dfs(String p){ 
        //재귀시 u,v 초기화 확인, u 에 붙여야 하니까 새 변수 할당 고민
            int count = 0;

            //P 올바른 문자열 검사
            if (rightString(p)) { //종료조건
                return p;
            }

            //두 균형잡힌 문자열로 분리
            for (int i = 0; i < p.length(); i++) {
                if (p.charAt(i) == '(') {
                    count++;
                } else if (p.charAt(i) == ')') {
                    count--;
                }
                if (count == 0) {
                    u = p.substring(0, i + 1);
                    v = p.substring(i + 1);
                    break;
                }
            }

            //u 올바른 문자열 검사
            if (rightString(u)) { //u 가 올바른 문자열일 경우
                result += u + dfs(v); 
               // return result + dfs(v);
            }
            else {
                //u 가 올바른 문자열 x -> 빈 문자열에 ( 붙임, 이거 순서 고민
                u = u.substring(1, u.length()-1 );
                String nuwU ="";
                for (int i = 0; i < u.length(); i++) {
                    if (u.charAt(i) == '(') {
                        nuwU += ')';
                    } else {
                        nuwU += '(';
                    }
                }
                result = result + '(' + dfs(v) + ')' + nuwU;
               // return result + '(' + dfs(v) + ')' + nuwU;
            }
            return result; 
        }
        
        //올바른 문자열 검사
        public static boolean rightString(String u){
            stack.clear();
            for(int i =0; i<u.length(); i++){
                if(u.charAt(i)=='('){
                    stack.push('(');
                }
                else{
                    if(!stack.isEmpty()) {
                        stack.pop();
                    }
                }
            }
            return stack.isEmpty();
        }
    
}
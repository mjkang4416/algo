import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
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
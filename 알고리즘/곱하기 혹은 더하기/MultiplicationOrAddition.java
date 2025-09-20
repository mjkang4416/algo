import java.util.Scanner;

public class MultiplicationOrAddition {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String st = sc.next();

        int[] num = new int[st.length()];

        for(int i =0; i<st.length(); i++){
            num[i] = st.charAt(i)-'0'; // 빼주는거 주의
        }

        for(int i=0; i<st.length()-1; i++){
            if(num[i]!=0 && num[i+1] !=0 && num[i] !=1 && num[i+1] !=1){
                num[i+1] = num[i] * num[i+1]; //
            }
            else{
                num[i+1] = num[i] + num[i+1];
            }
        }
        System.out.println(num[num.length-1]);
    }
}

import java.util.Scanner;

public class ReverseString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String S = sc.next();
        int refOne = 0;
        int refZero = 0;

        for(int i =0; i<S.length()-1; i++){
            if(S.charAt(i) != S.charAt(i+1)){
                if(S.charAt(i)=='1'){
                    refOne++;
                }
                else{
                    refZero++;
                }
            }
        }

        if(S.charAt(S.length()-1) != S.charAt(S.length()-2)){
            if(S.charAt(S.length()-2) == '1'){
                refZero++;
            }
            else{
                refOne++;
            }
        }

        System.out.println(Math.min(refZero, refOne));
    }
}

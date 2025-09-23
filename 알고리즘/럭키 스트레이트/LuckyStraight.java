import java.util.Scanner;

public class LuckyStraight {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        String strN = Integer.toString(N);


        int left = 0;
        int right = 0;

        for(int i =0; i<strN.length()/2; i++){
            left+= strN.charAt(i);
        }

        for(int i=strN.length()/2; i<strN.length(); i++){
            right+=strN.charAt(i);
        }

        if(left == right){
            System.out.println("LUCKY");
        }
        else{
            System.out.println("READY");
        }
    }
}

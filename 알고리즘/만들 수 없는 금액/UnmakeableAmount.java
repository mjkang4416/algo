import java.util.Arrays;
import java.util.Scanner;

public class UnmakeableAmount {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int [] arr = new int[N];

        int lastNum = 0;

        for(int i =0; i<N; i++){
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);

        for(int i =0; i<N; i++){
            if(lastNum+1 < arr[i]){
                break;
            }
            lastNum += arr[i];
        }

        System.out.println(lastNum+1);
    }
}

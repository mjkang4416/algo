import java.util.*;

public class ChoosingBowlingBall {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] arr = new int[N+1];

        int result = 0;
        
        for(int i =1; i<N+1; i++){
            arr[i] = sc.nextInt();
        }

        for(int i =1; i<N; i++){
            for(int j =i+1; j<N+1; j++){
                if(arr[i] == arr[j]){
                    continue;
                }
                result++;
            }
        }

        System.out.println(result);
    }
}

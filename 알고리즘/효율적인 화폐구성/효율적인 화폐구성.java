import java.util.Arrays;
import java.util.Scanner;

public class CoinComposition {
    public static void main(String[] args) {
        //N 종류 화폐 모아서 M 만들기
        //순서 구분 x

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] arr = new int[N];
        int[] result = new int[M+1];
        Arrays.fill(result, Integer.MAX_VALUE);

        for(int i = 0; i<N; i++){
            arr[i] = sc.nextInt();
        }

        result[0] = 0;

        Arrays.sort(arr);

        for(int i =0; i<N; i++){
            int coin = arr[i];
            for(int j = coin; j<M+1; j++){
                if (result[j - coin] + 1 < result[j] && result[j - coin] != Integer.MAX_VALUE) {
                    result[j] = result[j - coin] + 1;
                }
            }
        }

        if(result[M]==Integer.MAX_VALUE){
            System.out.println(-1);
        }
        else{
            System.out.println(result[M]);
        }


    }
}

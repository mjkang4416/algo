import java.util.Scanner;

public class TopToBottom {
    public static void main(String[] args) {
        //수열 큰 수 부터 작은 수로 정렬 (내림차순)
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] arr = new int[N];

        for(int i = 0; i<N; i++){
            arr[i] = sc.nextInt();
        }

        for(int i = 0; i<N; i++){
            for(int j = 0; j<i; j++){
                if(arr[i]>arr[j]){
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        for(int q = 0; q<N; q++){
            System.out.print(arr[q]);
            System.out.print(" ");
        }

    }
}

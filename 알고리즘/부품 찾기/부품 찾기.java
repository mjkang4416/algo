import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;

public class FindParts {
    public static boolean binary_search(int start, int end, int target, int[] allParts) {
        if (start > end) {
            return false;
        }
        int mid = (start + end) / 2;
        // mid 가 찾던 숫자면
        if (allParts[mid] == target) {
            return true;
        }
        // 찾으려는 값이 중간보다 작은경우
        else if (allParts[mid] > target) {
            return binary_search(start, mid - 1, target, allParts);
        }
        // 찾으려는 값이 중간보다 큰 경우
        else{
            return binary_search(mid + 1, end, target, allParts);
        }
    }


    public static void main(String[] args) {
        // N = 부품 개수
        // 각 부붚은 고유한 번호가 있움
        // 손님이 M 개 종류 부품 대량 구매 할때 푸품 있으면 yes 없으면 no 출력

        Scanner sc = new Scanner(System.in);


        int N = sc.nextInt();
        int[] allParts = new int [N];


        for(int i = 0; i<N; i++){
            allParts[i] = sc.nextInt();
        }

        int M = sc.nextInt();
        int [] orderParts = new int[M];
        int target;

        for(int j=0; j<M; j++){
            orderParts[j] = sc.nextInt();
        }

        Arrays.sort(allParts);

        for(int k =0; k<M; k++){
            target = orderParts[k];
            System.out.println(binary_search(0, N - 1, target, allParts) ? "yes" : "no");
        }
    }
}

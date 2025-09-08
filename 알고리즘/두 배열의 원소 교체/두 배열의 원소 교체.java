import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class SwappingElementsTwoArrays {
    public static void main(String[] args) {
        //배열 A 와 B 의 원소를 k 번 바꿔치기 해서 A의 원소 합을 최대로 만들자.
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); //두개의 배열 개수
        int[] A = new int [N];
        Integer[] B = new Integer[N];
        int K = sc.nextInt();
        int result = 0;

        for(int i =0; i<N; i++){
            A[i] = sc.nextInt();
        }
        for(int j = 0; j<N; j++){
            B[j] = sc.nextInt();
        }

        Arrays.sort(A); //오른차순 정렬
        Arrays.sort(B, Comparator.reverseOrder());  //내림차순 정렬

        for(int q = 0; q<K; q++){
            A[q] = B[q]; //레퍼런스 타입이지만 오토 언박싱 일어나서 ㄱㅊ 
        }

        for(int k =0; k<N; k++){
            result+= A[k];
        }

        System.out.println(result);
    }
}

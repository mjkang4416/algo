import java.util.Arrays;
import java.util.Scanner;

public class AdventurerGuild {
    public static void main(String[] args) {
        // 모험가수 : N
        // 공포도 : X
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] X = new int[N];

        for (int i=0; i<N; i++) { //각 모험가 공포도
          X[i] = sc.nextInt();
        }

        Arrays.sort(X); //오름차순 정렬
        //2 3 4 7 8 8 8 8
        //낮은거부터 묶어서 보내자 공포도 같은게 있을 수도 있음

        int result = 0;
        int count = 0;
        for(int i=0; i<N; i++){
            count++;
            if(count >= X[i]){
                result++;
                count = 0;
            }
        }
        System.out.println(result);
    }
}

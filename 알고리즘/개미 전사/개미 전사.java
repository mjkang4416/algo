import java.util.Scanner;

public class Mildsalmon {
    public static void main(String[] args) {
        // 식량창고 N 개
        // 각 식량창고에 저장된 식량 개수 K
        // 인접한거 들리면 x -> 가장 식량 많이 얻을 수 있도록

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] wareHouse = new int[N];
        int[] d = new int[N+1];

        for(int i =0; i<N; i++){
            wareHouse[i] = sc.nextInt();
        }

        d[0] = wareHouse[0];

        d[1] = Math.max( wareHouse[0],wareHouse[1]); //1인덱스가 마지막 일때 식량 최댓값 0이 더 크면 0 선택하는 것 임으로 둘중 큰거


        for(int i=2; i<N; i++){
            d[i] = Math.max(d[i-1],wareHouse[i]+d[i-2]); //직전거의 최댓값 을 선택할지 현재 -2 +현재값 의 최댓값을 선택할지 max 를 구함
            // 더해지면서 최댓값이 업데이트 되기때문에 2~N 까지 각 항의 최댓값이 나옴
        }
        System.out.println(d[N-1]);
    }
}

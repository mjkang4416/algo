import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[] house;

    static int  mid ;

    public static void main(String[] args) throws IOException {
        //특정 위치의 집에 안테나 설정
        //안테나로부터 모든 집까지 거리가 최소
        //이 때 안테나는 집이 위치한 곳에만 설치할 수 있고, 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능하다.
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

         N = Integer.parseInt(st.nextToken());
         house = new int[N];

        st = new StringTokenizer(bf.readLine());

        for(int i =0; i<N; i++){
            house[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(house); //오름차순 정렬 1,5,7,9

        sort();

        System.out.println(house[mid]);
    }

    public static void sort(){
        mid = N/2; //집 개수가 홀수일때 인덱스
       if(N%2 == 0){ //집 개수가 짝수일때
           int sum1 = 0;
           for(int i =0; i<N; i++){
               sum1 += Math.abs(house[mid]-house[i]);
           }

           int sum2 = 0;

           mid--;
           for(int i =0; i<N; i++){
               sum2 += Math.abs(house[mid]-house[i]);
           }

           if(sum1 < sum2){
               mid ++;
           }
       }
    }
}

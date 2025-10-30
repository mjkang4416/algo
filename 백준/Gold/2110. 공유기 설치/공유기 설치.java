import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int c;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        n = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        int[] arr = new int [n];

        for(int i=0; i<n; i++){
            arr[i] =  Integer.parseInt(bf.readLine());
        }

        //집들 오름차순 정렬
        Arrays.sort(arr);

        int lo = 1; //가능한 최소 간격
        int hi = arr[n-1]-arr[0]; //입력받은 집들의 최대 간격

        while (lo <= hi){ //최소 간격이, 최대 간격보다 작거나 같은 동안 , 즉 더 커지면 멈춘다.{
            //모든 간격 경우의 수 다 구해보는것.
            int mid = (lo+hi)/2; //최소거리 설정
            int position =0; //첫번쨰 집에 하나 설치
            int cnt =1; //설치 가능한 공유기 개수
            for(int i =1; i<n; i++){
                if(arr[i]-arr[position] >= mid){ //mid 이상 떨어져 있으면 공유기 설치
                    position = i;
                    cnt ++;
                }
            }
            if(cnt < c ){
                hi = mid -1;
                continue;
            }
            lo = mid+1;
        }

        System.out.print(lo-1);
    }
}

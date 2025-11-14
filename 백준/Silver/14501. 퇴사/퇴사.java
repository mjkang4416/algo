import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n;

    static int[]t;
    static int[]p;

    static int[]dp;

    public static void main(String[] args) throws IOException {
        //오늘부터 N+1 일째 되는 날 퇴사 -> 오늘부터 N 일까지 다닌다.
        //최대수익
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(bf.readLine());


        t = new int[n];
        p = new int[n];
        dp = new int[n+1];

        for(int i =0; i<n; i++){
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int time = Integer.parseInt(st.nextToken());
            int price = Integer.parseInt(st.nextToken());

            t[i] = time;
            p[i] = price;
        }
        for(int i =0; i<n; i++){ //원래 0 자리엔 0일 이니까 아무것도 안 들어오는거.
            if(i+t[i] <=n){
                dp[i+t[i]] = Math.max(dp[i+t[i]],dp[i]+p[i]);
            }

            dp[i+1] = Math.max(dp[i],dp[i+1]);
        }
        System.out.println(dp[n]);
    }
}

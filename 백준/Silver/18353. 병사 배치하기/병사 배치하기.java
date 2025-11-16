import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
         //병사 N 명
        // 각 병사당 전투력 보유
        // 병사 배치는 전투력 높은거부터 내림차순
        // 배치할때 특정 위치에 있는 병사는 열외
        // 남아있는 병사의 수가 최대가 되도록
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());
        int[] powers = new int[n];
        int[] dp = new int[n];

        StringTokenizer st = new StringTokenizer(bf.readLine());
        for(int i =0; i<n; i++){
            powers[i] = Integer.parseInt(st.nextToken());
        }

        int exceptionNum = 0;

        //제일 긴 내림차순 수열 찾기
        for(int i =0; i<n; i++){
            dp[i] = 1;
            for(int j=0; j<i; j++){
                if(powers[j]>powers[i]){
                    dp[i] = Math.max(dp[i],dp[j]+1); //j+1 이면 i 이전 j 문자열을 하나 i 에 포함하는것
                }
            }
            exceptionNum = Math.max(exceptionNum,dp[i]);
        }
        System.out.println(n-exceptionNum);
    }
}

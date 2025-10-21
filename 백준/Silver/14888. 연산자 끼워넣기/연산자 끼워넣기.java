import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] arr;
    static int[] operatorNum;
    static int N;
    static  int min = Integer.MAX_VALUE;
    static int max = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken()); //숫자개수

        arr = new int[N]; //숫자

        st = new StringTokenizer(bf.readLine());
        for(int i =0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        operatorNum = new int[4]; //연산자 개수

        st = new StringTokenizer(bf.readLine());
        for(int i =0; i<4; i++){
            operatorNum[i] = Integer.parseInt(st.nextToken());
        }

        dfs(0,arr[0]);

        System.out.println(max);
        System.out.println(min);
    }

    public static void dfs(int idx,int num){

        if(idx == N-1){ //하나의 정렬이 끝난 경우
            min = Math.min(num, min);
            max = Math.max(num,max);
        }
        else{
            for(int i =0; i<4; i++){ //연산자 넣는 경우의 수 계산
                if(operatorNum[i] <= 0){ //해당 위치가 0 인 경우
                    continue;
                }
                operatorNum[i]--; //아니면 -- 해주고
                if(i==0){
                    dfs(idx+1,num + arr[idx+1]); //알맞은거 selected
                }else if (i==1) {
                    dfs(idx+1,num - arr[idx+1]); //알맞은거 selected
                }else if (i==2) {
                    dfs(idx+1,num * arr[idx+1]); //알맞은거 selected
                }else {
                    dfs(idx+1,num / arr[idx+1]); //알맞은거 selected
                }
                operatorNum[i]++;
            }
        }
    }
}

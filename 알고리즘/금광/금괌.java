import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class GoldMine {
    static int T;

    static int[][] AllResult;

    static List<Integer> maxResult = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        //n*m 크기의 금광 -> 열개수만큼 이동
        //첫번째 열부터 시작해서 캠
        //첫번째 열의 어느 행에서든 시작 가능
        //m 번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 위치중 하나로 이동
        //채굴자가 얻을 수 있는 금의 최대 크기
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(bf.readLine());

        for(int i =0; i<T; i++){
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            int[][] arr =  new int[n][m];

            st = new StringTokenizer(bf.readLine());
            for(int j=0; j<n; j++){
                for(int k =0; k<m; k++){
                    arr[j][k] = Integer.parseInt(st.nextToken());
                }
            }

            dp(arr,n,m); //금 찾기
        }

        for(int result : maxResult){
            System.out.println(result);
        }
    }
    public static void dp( int [][] arr,int n,int m){
        AllResult = new int[n][m]; // arr 배열을 결과 배열에 복제
        for(int i =0; i<n; i++){
            AllResult[i] = arr[i].clone();
        }

        for(int i =1; i<m; i++){ //열 하나씩 이동
            for(int j=0; j<n; j++){ //행 하나씩 이동
              if(j==0) //첫번째 행인 경우
              {
                    AllResult[j][i] += Math.max(AllResult[j][i-1] , AllResult[j+1][i-1]);
              }
              else if(j == n-1){ //마지막 행인 경우,
                    AllResult[j][i] += Math.max(AllResult[j][i-1], AllResult[j-1][i-1]);

              }
              else{ //중간 행인 경우
                      AllResult[j][i] += Math.max(AllResult[j][i-1], Math.max(AllResult[j-1][i-1], AllResult[j+1][i-1]));
              }
            }
        }
        int result = AllResult[0][m-1];
        for(int j =1; j<n; j++){
            result = Math.max(result, AllResult[j][m-1]);
        }
        maxResult.add(result);
    }
}

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine().trim());

        int[][][] resultArr = new int[T][][];

        for(int i =0; i<T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int[][] arr = new int[N][N]; //배열 입력
            for (int k = 0; k < N; k++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    arr[k][j] = Integer.parseInt(st.nextToken());
                }
            }

            int[][] result = arr.clone(); // 원본을 카피 해 놓은 결과 배열
            for(int k =0; k< N; k++){
                result[k] = arr[k].clone();
            }

            int rotateNum = 0;//몇번 돌려야 할지 산정

            if(d <0){
                rotateNum = (-d) / 45;
                for(int num =0; num<rotateNum; num++){ // 횟수만큼 배열 회전
                    result = rotate(result,false);
                }
            }
            else{
                rotateNum = d/ 45;
                for(int num =0; num<rotateNum; num++){ // 횟수만큼 배열 회전
                    result = rotate(result,true);
                }
            }

            resultArr[i] = result;
        }
        // 완성된 배열 print
        for(int j = 0; j<T; j++){
            for(int k =0; k<resultArr[j].length; k++){
                for(int q =0; q<resultArr[j].length; q++){
                    System.out.print(resultArr[j][k][q]+" ");
                }
                System.out.println();
            }
        }
    }

    public static int[][] rotate(int[][] arr,boolean bool){ //여기서 출력까지 해줘야
        //원래배열 카피해서 가지고 있고 원래 배열에서 가져와서 바꿈
        int[][] result = arr.clone(); // 원본을 카피 해 놓은 결과 배열
        for(int k =0; k< arr.length; k++){
            result[k] = arr[k].clone();
        }
        //좌표 맵핑 헷갈리니까 미리 변수로 만들어 놓는게 낫겠다.


        if(bool) { //시계방향
            for (int i = 0; i < arr.length; i++) {
                result[i][arr.length / 2] = arr[i][i];  //주대각 -> 가운데열
                result[i][arr.length - i - 1] = arr[i][arr.length / 2];   //가운데열 -> 부대각
                result[arr.length / 2][arr.length - i - 1] = arr[i][arr.length - i - 1]; //부대각 -> 가운데행
                result[i][i] = arr[arr.length / 2][i]; //가운데행-> 주대
            }
        }
        else{ //반시계 방향
            for(int i =0; i<arr.length; i++){
                result[arr.length/2][i] = arr[i][i];  //주대각 -> 가운데행
                result[i][i] = arr[i][arr.length/2];   //가운데열 -> 주대각
                result[i][arr.length/2] = arr[i][arr.length-i-1]; //부대각 -> 가운데열
                result[i][arr.length - i - 1] = arr[arr.length/2][arr.length-i-1]; //가운데행-> 부대
            }
        }

        return result;
    }
}

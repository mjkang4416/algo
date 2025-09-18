import java.util.Scanner;


public class FutureCity {
    public static void main(String[] args) {
        //n 개의 노드가 있을때 k 를 거쳐서 x 로 가는 최소 이동시간
        //시간은 간선을 기준으로 한다.

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 노드개수
        int M = sc.nextInt(); // 간선개수
        int[][] arr = new int[N+1][N+1];
        int INF = (int) 1e9;

        for(int i =1; i<N+1; i++){ // 자기자신 빼고 전부 Inf 로 초기화
            for(int j=1; j<N+1; j++){
                if(i!=j){
                    arr[i][j] = INF;
                }
            }
        }

        for(int i =0; i<M; i++){ // 간선 입력 받고 arr 메트릭스에 표기
            int a = sc.nextInt();
            int b = sc.nextInt();

            arr[a][b] = 1;
            arr[b][a] = 1;
        }

        for(int k =1; k<N+1; k++){
            for(int a=1; a<N+1; a++){
                for(int b=1; b<N+1; b++){
                    arr[a][b] = Math.min(arr[a][b],arr[a][k]+arr[k][b]);
                }
            }
        }

        int X = sc.nextInt();
        int K = sc.nextInt();

        int result = arr[1][K]+arr[K][X];

        if(result >= INF){
            System.out.println(-1);
        }
        else{
            System.out.println(result);
        }

    }
}


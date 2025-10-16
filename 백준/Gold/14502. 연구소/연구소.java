import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int M;

    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};

    static int[][] map;
    static int [][] copyMap;

    static int maxSafetyRoom = Integer.MIN_VALUE;
    public static Queue<Virus> qu = new LinkedList<Virus>();

     static class Virus{
        int x;
        int y;

         Virus(int x, int y){
             this.x = x;
             this.y = y;
         }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];

        for(int i =0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j =0; j<M; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        def(0,0);
        System.out.println(maxSafetyRoom);
    }

    public static void def(int wallCount , int start){ //dfs 로 조합을 구현한것.
        if(wallCount==3){ //백 3개를 다 세웠을때
            bfs(); //bfs 로 전파 검사
            return;
        }
        for(int i =start; i< N*M; i++){ //2차원 배열 평탄화 -> 조합 구성
            int r = i / M, c = i % M;
                if(map[r][c] == 0){
                    map[r][c] = 1;
                    def(wallCount+1, start+1);
                    map[r][c] = 0;
                }
        }
    }

    public static void bfs(){ //bfs 로 바이러스 전파
        for(int i =0; i<N; i++){ //큐에 바이러스 삽입
            for(int j =0; j<M; j++){
                if(map[i][j]==2){
                    qu.add(new Virus(i,j));
                }
            }
        }

        copyMap = new int[N][M];

        for(int i =0; i<N; i++){
            copyMap[i] = map[i].clone();
        }


        while (!qu.isEmpty()){
            Virus v = qu.poll();

            for(int i=0; i<4; i++){
                int nx = v.x+ dx[i];
                int ny = v.y + dy[i];

                if(nx>=0 && ny>=0&& nx<N && ny<M){
                    if(copyMap[nx][ny]==0){
                        copyMap[nx][ny]= 2;
                        qu.add(new Virus(nx,ny));
                    }
                }

            }

        }

        stfeZone(copyMap);
    }
    static void stfeZone(int[][] copyMap){
         int safeCount = 0;
         for(int i =0; i<N; i++){
             for(int j =0; j<M; j++){
                 if(copyMap[i][j]==0){
                     safeCount++;
                 }
             }
         }
         maxSafetyRoom = Math.max(safeCount,maxSafetyRoom);
    }


}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int K;
    static int[][] arr;

    static Queue<Virus2> qu = new LinkedList<>();

    static int S;
    static int X;
    static int Y;

    static int[] dx = {0,0,-1,1};
    static int[] dy = {1,-1,0,0};

    static int time = 0;

    static int num = 0;

    static class Virus2{
        int x;
        int y;
        int virusNum;

        int time;

        Virus2(int x, int y,int virusNum){
            this.x = x;
            this.y = y;
            this.virusNum = virusNum;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new int [N][N];

        for(int i =0; i<N; i++){
            st = new StringTokenizer(bf.readLine());
            for(int j =0; j<N; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        st = new StringTokenizer(bf.readLine());

        S = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());
        Y = Integer.parseInt(st.nextToken());

        bfs();

        if(arr[X-1][Y-1]!=0){
            System.out.println(arr[X-1][Y-1]);
        }
        else {
            System.out.println(0);
        }
    }

    public static void bfs(){
        ArrayList<Virus2> v = new ArrayList<>();
        for(int i =0; i<N; i++){ //큐에 바이러스 넣기 , priority queue 라서 오른차순 정렬
            for(int j=0; j<N; j++){
                if(arr[i][j]!=0){
                    v.add(new Virus2(i,j,arr[i][j]));
                }
            }
        }

        Collections.sort(v,Comparator.comparingInt(o1->o1.virusNum));

        for (Virus2 virus2 : v) {
            qu.add(virus2);
        }

        num = qu.size();

        int newNodeNum = 0;

        while (!qu.isEmpty()) {

            if(time == S){
                break;
            }

            Virus2 virus = qu.poll();
            num --;


            for (int i = 0; i < 4; i++) { //뽑은 바이러스 상하좌우 방향으로 번지게
                int nx = virus.x + dx[i];
                int ny = virus.y + dy[i];

                if (nx >= 0 && ny >= 0 && ny < N && nx < N) {
                    if (arr[nx][ny] == 0) { //상하좌우 중 하나의 공간이 0 일 경우
                        arr[nx][ny] = arr[virus.x][virus.y];
                        newNodeNum++;
                        qu.add(new Virus2(nx, ny, arr[virus.x][virus.y]));
                    }
                }
            }
            if(num==0){ //한 회를 다 돌았을때
                time ++;
                num = newNodeNum;
                newNodeNum = 0;
            }

        }

    }
}

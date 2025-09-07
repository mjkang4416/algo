import com.sun.source.tree.TryTree;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;


public class EscapeMaze {
    //N*M 크기 미로
    //현 위치 (1,1)
    //출구는 (N,M)
    //한번에 한칸씩 이동
    //1 이 있는 자리로만 이동 가능
    //총 움직여야 하는 최소 개수

    static int N;
    static int M;
    static int [][] maze;

    static int xPos;
    static int yPos;



    public static class Pair{
        int x;
        int y;

        public Pair(int y, int x) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            return super.equals(obj);
        }
    }

    public static int bfs(Pair pair) {

        Queue<Pair> queue = new LinkedList<>();
        int[] xMaze = new int[]{-1, 1, 0, 0};
        int[] yMaze = new int[]{0, 0, -1, 1};

        queue.add(pair);

        //dfs 로 탐색
        while (true) {

            pair = queue.remove();

            if (pair.x == M - 1 && pair.y == N - 1) {
                return maze[pair.y][pair.x];
            }

            for (int i = 0; i < 4; i++) {
                xPos = pair.x + xMaze[i];
                yPos = pair.y + yMaze[i];

                //배열을 넘어가는 경우, 0으로 막혀 있는 경우
                if (xPos < 0 || xPos >= M || yPos < 0 || yPos >= N) {
                    continue;
                }

                if (maze[yPos][xPos] == 0) { //인덱스 에러 때문에 분리
                    continue;
                }

                if (maze[yPos][xPos] == 1) { //아직 방문 안한거면
                    Pair pair1 = new Pair(yPos, xPos);
                    queue.offer(pair1); //상하좌우 돌면서 근처에 값 있으면 큐에 넣음
                    maze[yPos][xPos] = maze[pair.y][pair.x] + 1; //이전에 뽑은거에서 1 증가
                }
            }
        }

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        maze = new int[N][M];

        for(int i =0; i<N; i++){
            for(int j = 0; j<M; j++){
                maze[i][j] = sc.nextInt();
            }
        }
        Pair pair = new Pair(0,0);
        //시작칸부터 bfs 시작
        System.out.println(bfs(pair));

    }
}

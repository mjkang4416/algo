import java.util.Scanner;

public class GameDevelopment {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 세로
        int M = sc.nextInt(); // 가로

        int A = sc.nextInt(); // 좌표 A
        int B = sc.nextInt(); // 좌표 B
        int d = sc.nextInt(); // 방향 d

        int [][] map = new int[N][M];
        int visitCount = 0;
        int turnCount = 4;

        for(int i =0; i<N; i++){ //map 받기
            for(int j=0; j<M; j++){
                map[i][j] = sc.nextInt();
            }
        }

        int[] direction = new int []{0,3,2,1}; //북,서,남,동 순서대로 이동하게
        int[][] x = new int [][]{{0,-1},{-1,0},{0,1},{1,0}}; //direction 값이 인덱스로 올때 이동거리

        boolean point = true;

        map[A][B] = 1; //맨 첫자리 갔다고 표시
        visitCount++; //방문횟수 증가


        while (point){
            if(d == 3){
                d = 0;
            }
            else{
                d++;
            }
            int a = A+x[direction[d]][0]; //회전 후 위치 이동
            int b = B+x[direction[d]][1];

            //이동할 길이 있는 경우
            if(a >= 0 && a < N && b >= 0 && b < M && map[a][b] == 0){
                A = a;
                B = b;
                map[A][B] = 1;
                turnCount = 0;
                visitCount ++;
                continue;
            }
            //왼쪽 방향으로 못가는 경우
            if(a >= 0 && a < N && b >= 0 && b < M && map[a][b] == 1){
                //방향 유지한채로 1단계로
                turnCount --;

                // 4 방향 모두 못가는 경우 뒤로 바꾼 방향 유지한 채로 1 단계로
                if(turnCount == 0){
                    a=A-x[direction[d]][0];
                    b=B-x[direction[d]][1];
                    // 뒤로 못가는 경우 멈춤
                    if(map[a][b] == 1){
                        break;
                    }
                    A = a;
                    B = b;
                    turnCount = 4;
                }
            }

        }

    System.out.println(visitCount);
    }
}

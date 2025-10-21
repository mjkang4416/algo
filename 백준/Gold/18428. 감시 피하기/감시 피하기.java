import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static char[][] arr;
    static Queue<Techer> qu = new LinkedList<>();

    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static String result = "NO";

    static class Techer {
        int x;
        int y;

        Techer(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken());

        arr = new char[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(bf.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = st.nextToken().charAt(0);
            }
        }


        dfs(0, 0);
        // 복도에서 정확히 3 개 위치에 장애물 설치 -> 모든 학생들이 감시 피할 수 있도록
        // 완탐 , 모든 위치에 다 3개의 장애물 세워 봐야 할듯 ? 조합으로

        System.out.println(result);

    }

    public static void dfs(int start, int idx) { //완탐 위한 조합
        //3개의 장애물 dfs 로 조합
        if (idx == 3) { //3개 다 선택 된 경우
            if(check()){
               result = "YES";
            }
        } else {
            for (int i = start; i < N * N; i++) { //조합 -> 2차원 평탄화
                int x = i / N, y = i % N;
                if (arr[x][y] == 'X') {
                    arr[x][y] = 'O';
                    dfs(i + 1, idx + 1);
                    arr[x][y] = 'X';
                }
            }
        }
    }

    public static boolean check() { //true false 체크

        for (int i = 0; i < N; i++) { //T 위치 찾아서 큐에 넣기
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == 'T') {
                    qu.add(new Techer(i, j));
                }
            }
        }

        while (!qu.isEmpty()) { // false 에 안걸리면 무조건 true
            Techer t = qu.remove();

            for (int i = 0; i < 4; i++) { //T 큐에서 뽑아서 상 하 좌 우 전체를 N 크기 검사
                int x = t.x;
                int y = t.y;
                for (int j = 0; j < N; j++) { //한 방향을 N 크기 검사
                    x += dx[i];
                    y += dy[i];

                    if (x < 0 || y < 0 || x >= N || y >= N) { //사이즈 넘어가면 break
                        break;
                    }

                    if (arr[x][y] == 'O') { //벽 있으면 어짜피 false 일 수 없음
                        break;
                    } else if (arr[x][y] == 'S') {
                        return false;
                    }
                }
            }
        }
        return true;
    }

}

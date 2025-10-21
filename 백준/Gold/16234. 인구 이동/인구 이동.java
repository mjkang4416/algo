import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    static int N;

    static int L;
    static int P;

    static int[][] arr;

    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,-1,1};

    static boolean[][] visited;

    static LinkedList<Contry> selected = new LinkedList<>();

    static int day=0;

    static class Contry {
        int x;
        int y;
            Contry(int x, int y) {
                this.x = x;
                this.y = y;
            }
    }
        public static void main(String[] args) throws IOException {

            BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(bf.readLine());

            N = Integer.parseInt(st.nextToken());
            L = Integer.parseInt(st.nextToken());
            P = Integer.parseInt(st.nextToken());

            arr = new int[N][N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(bf.readLine());
                for (int j = 0; j < N; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            while (true) { //이동이 없을때까지 계속 돈다.
                visited = new boolean[N][N]; //방문상태 초기화
                boolean flag = false; // check 했을때 바뀐게 있는지

                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < N; j++) { //다 돌면서 visited 되지 않은거 찾아서 dfs 뭉탱이
                        if (!visited[i][j]) {
                            dfs(i, j);
                            if (selected.size()>1) { //select 된게 있으면 바뀐거
                                flag = true;
                                check();
                            }
                            selected.clear(); //선택된거 초기화
                        }
                    }
                }
                if (!flag) {
                    break;
                } else {
                    day++;
                }
            }
            System.out.println(day);
        }

        public static void dfs(int x, int y) {

            visited[x][y] = true; //방문시 true 방문노드 표시
            selected.add(new Contry(x, y));

            //해당 노드에서 상하좌우 이동
            for (int i = 0; i < 4; i++) {
                int newX = x + dx[i];
                int newY = y + dy[i];

                if (newX < 0 || newY < 0 || newX >= N || newY >= N) { //해당 노드의 상하좌우 사이즈 검사
                    continue;
                }
                if (visited[newX][newY]) { //해당 노드의 상하좌우 방문 검사
                    continue;
                }

                //상하좌우 차이 검사
                int valid = Math.abs(arr[x][y] - arr[newX][newY]);
                if (valid >= L && valid <= P) {
                    dfs(newX, newY);
                }
            }

        }

        public static void check() { //추가된 노드 합치기
            int sum = 0;
            for (int i = 0; i < selected.size(); i++) {
                int x = selected.get(i).x;
                int y = selected.get(i).y;

                sum += arr[x][y];
            }

            int result = sum/selected.size();
            for (Contry contry : selected) {
                int x = contry.x;
                int y = contry.y;

                arr[x][y] = result;
            }

        }

}

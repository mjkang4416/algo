import java.security.PublicKey;
import java.util.Scanner;

public class FreezingDrink {
    // n*m 크기 얼음틀 구멍뚤린건 0 칸막이 있는건 1
    // 구멍 뚤린 부분끼리 상,하,좌,우 로 붙어있는 경우 연결된 거라고 생각함
    // 생성되는 총 아이스크림 개수는 ?

    private static int N;
    private static int M;
    private static int[][] iceCubeTray;
    private static int result;

    public static boolean dfs(int i, int j) {

        if(i<0 || i>=N || j<0 || j>=M ){
            return false;
        }

        //진입시에 검사 하지만, 내부적으로 재귀호출 되기 때문에 여기서 검사 해줘야
        if(iceCubeTray[i][j]==0) {
            iceCubeTray[i][j] = 1;

            //스텍에 인접한 거부터 넣고 , 뺀 노드와 인접한걸 찾으면서 0이 없을 때 까지 진행 , 스택 = 재귀로 가능
            dfs(i+1,j);
            dfs(i-1,j);
            dfs(i,j+1);
            dfs(i,j-1);

            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt(); // 얼음틀 세로 길이
        M = sc.nextInt(); // 얼음틀 가로 길이

        iceCubeTray = new int[N][M];
        result = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                iceCubeTray[i][j] = sc.nextInt();
            }
        }

        //전체 배열을 돌면서 0 인걸 찾는다
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                // 이미 visit 된 경우 다음 칸으로 넘어간다
                if (iceCubeTray[i][j] == 1) {
                    continue;
                }
                // visit 되지 않고 0 이 나올 경우 dfs 를 실시한다.
                if (dfs(i, j)) {
                    result++;
                }
            }
        }
        System.out.println(result);
    }
}

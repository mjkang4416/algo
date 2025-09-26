import java.util.Scanner;

public class RepaintChessboard {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        char[][] arr = new char[N][M];
        int result = 999999999;

        for(int i =0; i<N; i++){
            String line = sc.next();
            for(int j=0; j<M; j++){
                arr[i][j] = line.charAt(j);
            }
        }

        for(int i =0; i<=N-8; i++) { //완전탐색
            for (int j = 0; j <=M-8; j++) { //하나씩 내리면서 가로로 탐색
                int wResult = 0;
                int bResult = 0;
                int count = 0;

                //첫칸이 하얀색일 경우 계산
                    char[][] tempArr1 = arr.clone();
                    for(int k = 0; k < N; k++) {
                        tempArr1[k] = arr[k].clone();
                    }
                    if(tempArr1[i][j] != 'W'){
                        tempArr1[i][j] = 'W';
                        wResult++;
                    }
                    wResult += test(tempArr1, i, j);

                //첫칸이 검은색일 경우 계산
                    char[][] tempArr2 = arr.clone();
                    for(int k = 0; k < N; k++) {
                        tempArr2[k] = arr[k].clone();
                    }
                    if(tempArr2[i][j] != 'B'){
                        tempArr2[i][j] = 'B';
                        bResult++;
                    }
                    bResult += test(tempArr2, i, j);

                count = Math.min(wResult, bResult);
                result = Math.min(result,count);
            }
        }
        System.out.println(result);
    }

    public static int test(char[][] arr, int i, int j) {
        int count = 0;
        for (int x = 0; x < 8; x++) { //8*8 전체탐색
            for (int y = 0; y < 8; y++) {
                if (x <7 && arr[i + x][j] == arr[i + x + 1][j]) { //첫줄과 다음줄의 첫문자가 같은경우
                    count++;
                    if (arr[i + x][j] == 'W') {
                        arr[i + x + 1][j] = 'B';
                    } else {
                        arr[i + x + 1][j] = 'W';
                    }
                }
                if (y<7 && arr[i + x][j + y] == arr[i + x][j + y + 1]) { //이번 문자와 다움 문자가 같은 경우
                    count++;
                    if (arr[i + x][j + y] == 'W') {
                        arr[i + x][j + y + 1] = 'B';
                    } else {
                        arr[i + x][j + y + 1] = 'W';
                    }

                }
            }
        }
        return count;
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Node3{
    int x;
    int y;

    Node3(int x, int y){
        this.x =x;
        this.y = y;
    }
}
public class Main {
        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            int n = Integer.parseInt(br.readLine().trim());
            int k = Integer.parseInt(br.readLine().trim());
            int[][] appleSpot = new int[k][2]; //사과 위치
            int time = 0;

            Queue<Node3> qu = new LinkedList<>();
            int [][] arr = new int[n+1][n+1];
            int indexX = 1; //방문한 인덱스
            int indexY = 1;

            for(int i =0; i<k; i++){ //사과 위치 채우기
                StringTokenizer st = new StringTokenizer(br.readLine());
                appleSpot[i][0] = Integer.parseInt(st.nextToken());
                appleSpot[i][1] = Integer.parseInt(st.nextToken());
            }

            int l = Integer.parseInt(br.readLine().trim()); //뱀 방향변환 횟수
            char[]direction = new char[l];
            int[]dirTime = new int[l];

            for(int i =0; i<l; i++){ //시간과 방향 배열 채우기
                StringTokenizer st = new StringTokenizer(br.readLine()); // 앞에서 선언한 st 재사용
                dirTime[i] = Integer.parseInt(st.nextToken());
                direction[i] = st.nextToken().charAt(0);
            }

            int[] x = {-1,0,1,0}; //이동 가능한 경우의 수 짝
            int[] y = {0,1,0,-1}; //상,우,하,좌
            int head = 1;
            qu.add(new Node3(1,1));//(1,1)에 뱀을 초기화하지 않음 → qu.poll() 시 바로 NullPointerException 터질 수 있음.
            arr[1][1]=1;

            while(true){

                indexX += x[head];
                indexY += y[head];

                time++; // 이동 완료 후 시간 증가

                //  충돌 체크
                if (indexX < 1 || indexY < 1 || indexX > n || indexY > n) break;
                if (arr[indexX][indexY] == 1) break;

                boolean right = false;


                qu.add(new Node3(indexX,indexY)); //머리 추가
                arr[indexX][indexY] = 1;

                for(int i =0; i<k; i++){
                    if(indexX == appleSpot[i][0] && indexY == appleSpot[i][1]){ //사과 다음칸에 있는 경우 -> 해당칸1로 바꾸고 큐에 넣음
                        appleSpot[i][0] = -1; //이미 먹은 사과 없애줌
                        appleSpot[i][1] = -1;
                        right = true;
                    }
                }
                //사과 다음칸에 없는 경우 -> 큐에서 하나 빼고 해당 위치 0 으로 바꿈
                if(!right){
                    Node3 lastNode = qu.poll();
                    arr[lastNode.x][lastNode.y] = 0;
                }


                //다음 칸에서 방향전환 해야하는 경우
                for(int i=0; i<l; i++){
                    if(time == dirTime[i]){
                        dirTime[i] = -1;
                        if(direction[i]=='D'){
                            head ++;
                            direction[i] = ' ';
                        }
                        else{
                            head--;
                            direction[i] = ' '; }
                        if(head > 3){ //head 값 0,1,2,3 범위로 조정
                            head%=4;}
                        else if(head<0){head = 3;}
                    }
                }
            }
            System.out.println(time);
        }

}

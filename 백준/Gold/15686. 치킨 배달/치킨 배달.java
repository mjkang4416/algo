import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N ;
    static int M ;

    static int [][] arr;

    static ArrayList<NodeChicken> chickenArr;
    static ArrayList<NodeChicken> house;

    static boolean[] visited ;

    static ArrayList<NodeChicken> selected = new ArrayList<>();

    static int result  = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());


        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N][N];

        for(int i =0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j =0; j<N; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        chickenArr =  new ArrayList<>();
        house =  new ArrayList<>();

        for(int i =0; i<N; i++){ //치킨이랑 집 좌표 넣기
            for(int j=0; j<N; j++){
                if(arr[i][j] == 1){
                    house.add(new NodeChicken(i,j));
                }
                else if(arr[i][j]==2){
                    chickenArr.add(new NodeChicken(i,j));
                }
            }
        }

        visited = new boolean[chickenArr.size()];

        back(0,0);

        System.out.println(result);
    }

    public static void back(int start , int depth){

        if(depth == M){
            int sum = 0;
            for(int i =0; i<house.size(); i++){
                int min = Integer.MAX_VALUE;
                for(int j =0; j<selected.size(); j++){
                    // 하나의 집과 선택된 치킨집 들 사이의 최소 거리 구함
                    int d = Math.abs(house.get(i).x - selected.get(j).x) + Math.abs(house.get(i).y - selected.get(j).y);
                    min = Math.min(min,d);
                }
                sum+=min; //집마다 최소거리 합침
            }
            result = Math.min(result,sum); //이전 조합의 최소거리랑 이번 조합의 최소거리중 최소거리 구함
            return;
        }
        for(int i =start; i<chickenArr.size(); i++){ //치킨집 조합 구하기
            if(!visited[i]){
                visited[i] = true; //방문 했는지 표시
                selected.add(chickenArr.get(i)); //select list 에 치킨노드 넣어줌
                back(i+1,depth+1); //선택한 노드 다음부터 재귀
                selected.remove(selected.size()-1); //마지막 원소만 빼준다.
                visited[i] = false;
            }
        }
    }
}

class NodeChicken{
    int x;
    int y;

    public NodeChicken(int x, int y){
        this.x = x;
        this.y = y;
    }
}


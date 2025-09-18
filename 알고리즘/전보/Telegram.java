import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

class Node implements Comparable<Node>{ //node 객체

    public int index;
    public int distant;

    public Node (int index, int distant){
        this.index = index;
        this.distant = distant;
    }

    @Override
    public int compareTo(Node o) {
        return distant-o.distant;
    }
}

public class Telegram {
    static int N ;
    static int M ;
    static int C ;

    static ArrayList<ArrayList<Node>> arr = new ArrayList<ArrayList<Node>>();

    static int INF = (int)1e9;

    static int[] d;

    static PriorityQueue<Node> pq = new PriorityQueue<>();

    public static void dijkstra(int start){
        d[start] = 0; // 시작 노드로 가는 최단경로 0 처리
        pq.add(new Node(start,0)); //큐에 시작노드 넣기

        while(!pq.isEmpty()){
            Node node = pq.poll();
            // 현재 노드에서 해당 노드까지의 거리
            int distance = node.distant;
            int index = node.index;

            if(d[index]<distance){ //큐에서 뽑은 제일 작은 노드가 최소거리 list 의 해당노드 보다 크면 무시
                continue; //이미 거친 노드
            }

            for(int i =0; i<arr.get(index).size(); i++){ //그게 아니면 인접 list 순회
                int cost = d[index] + arr.get(index).get(i).distant; //뽑은 노드까지 오는 최소거리 + 인접리스트로 연결된 거리
                if(cost < d[arr.get(index).get(i).index]){ // 원래 있던 index 의 인접 list 거리보다 뽑은 노드를 거쳐가는게 작은경우
                    d[arr.get(index).get(i).index] = cost; //해당 인접리스트의 노드 cost 를 뽑은 노드를 거치는 거리로 바꿔줌
                    pq.offer(new Node(arr.get(index).get(i).index,cost)); //큐에 삽입
                }
            }

        }



    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
         N = sc.nextInt(); // 도시개수
         M = sc.nextInt(); // 간선개수
         C = sc.nextInt(); // 시작노드

        for(int i =0; i<N+1; i++){ // 그래프 초기화
            arr.add(new ArrayList<Node>());
        }

        for(int i=0; i<M; i++){ //간선 정보 입력받기
            int a = sc.nextInt(); //노드
            int b = sc.nextInt(); //b 노드로
            int c = sc.nextInt(); //간선

            arr.get(a).add(new Node(b,c));
        }

        d = new int[N+1];
        Arrays.fill(d, INF); // 최단거리 배열 INF 로 초기화

        dijkstra(C);

        int count =0;
        int time = 0;

        for(int i =0; i<N+1; i++){
            if(d[i]==INF){
                continue;
            }
            count++;
            time = Math.max(time,d[i]);
        }

        System.out.print((count - 1) + " " + time);

    }
}

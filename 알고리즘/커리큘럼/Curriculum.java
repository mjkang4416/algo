import java.util.*;


public class Curriculum {
    static int N;
    static int[] indegree;
    static ArrayList<ArrayList<Integer>> arr;

    static int[] time;


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt(); //노드 개수
        //간선 그래프 , 회색 표기 되는데 자바의 제네릭 타입 추론 기능 때문 이라고 함
        //자동 추론 함으로 굳이 작성할 필요 없어서 회색 표시 띄워준거임
        arr = new ArrayList<ArrayList<Integer>>();
        indegree = new int[N+1]; //진입차수 list
        time = new int[N+1]; // 시간 list

        Arrays.fill(indegree,0); //각 진입차수 0 으로 초기화

        for(int i=0; i<N+1; i++){
            arr.add(new ArrayList<>());
        }

        for(int i =1; i<N+1; i++){ // 각 강의 시간, 선수강 강의 입력

            int x = sc.nextInt(); // 각 강의 시간 입력
            time[i]  = x;

            while(true) // 선수과목 입력
            {
                int subject = sc.nextInt();
                if(subject==-1){
                    break;
                }
                arr.get(subject).add(i); //선수과목 추가
                indegree[i] +=1; //진입차수 증가
            }
        }
        topology_sort();
    }

    public static void topology_sort(){
        int[] result = time.clone(); //deep copy
        Queue<Integer> q = new LinkedList<>();

        for(int i =1; i<N+1; i++){ // 전체 돌면서 진입차수가 0 인 노드 큐에 넣기
            if(indegree[i] == 0){
                q.add(i);
            }
        }

        while(!q.isEmpty()){
            int now = q.poll();
            for(int sub : arr.get(now)){ //꺼낸 노드의 선수과목들 진입차수 --
                indegree[sub] --;
                result[sub] = Math.max(result[sub],result[now]+result[sub]); //선수과목들 중 시간이 큰걸 선택해서 현재 시간과 더해줌

                if(indegree[sub]==0){
                    q.add(sub);
                }
            }
        }
        for(int i = 1; i<N+1; i++){
            System.out.println(result[i]);
        }
    }
}

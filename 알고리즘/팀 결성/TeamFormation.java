import java.util.ArrayList;
import java.util.Scanner;


class ExclusiveNode {
    public int a;
    public int b;

    public int type;

    public ExclusiveNode(int type, int a, int b){
        this.type = type;
        this.a = a;
        this.b = b;
    }
}

public class TeamFormation {
    static int N;
    static int M;

    static ArrayList<ExclusiveNode> arr = new ArrayList<ExclusiveNode>();

    static int[] parents;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt(); //노드수
        M = sc.nextInt(); //연산수
        parents = new int[N+1]; //부모 집합

        for(int i =0; i<N+1; i++){ //부모집합 모두 자기 자신으로 채움
           parents[i] = i;
        }

        for(int i =0; i<M; i++){ //각 노드에 어떤 연산할지 받아옴
            int type = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();

            arr.add(new ExclusiveNode(type,a,b));
        }


        for(int i=0; i<M; i++){ // 각 노드에 어떤 연산할지 뽑아서
            int type = arr.get(i).type;
            int a = arr.get(i).a;
            int b = arr.get(i).b;

            if(type == 0){ //0 이면 해당 노드 합집합
                union(a,b);
            }
            else{ //아니면 find 연산
                if(find(a) == find(b)){ //a 와 b 의 부모노드가 같은 경우
                    System.out.println("YES");
                }
                else{
                    System.out.println("NO");
                }
            }
        }
    }

    private static int find(int a) {
        if(parents[a] != a){
            parents[a] = find(parents[a]);
        }
        return parents[a];
    }

    private static void union(int a, int b) {
        int parentA = find(a);
        int parentB = find(b);

        if(parentA < parentB){
            parents[b] = parents[a];
        }
        else{
            parents[a] = parents[b];
        }
    }
}

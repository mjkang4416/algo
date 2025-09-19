import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class CityDivisionPlan {
    static int N;
    static int M;
    static int[][] arr;

    static int[] parents;

    static int price;

    static int last;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();
        arr = new int[M][3];
        parents = new int[N+1];

        for(int i =0; i<N+1; i++){ //부모노드 자기자신으로 초기화
            parents[i] = i;
        }

        for(int i =0; i<M; i++) { // a 노드 -> b 노드 , 유지비
            int a = sc.nextInt();
            int b = sc.nextInt();
            int price = sc.nextInt();

            arr[i][0] = a;
            arr[i][1] = b;
            arr[i][2] = price;
        }

        Arrays.sort(arr, Comparator.comparingInt(o->o[2])); // price 기준으로 오름차순 정렬

        for(int i =0; i<M; i++) {
            if (find(arr[i][0]) == find(arr[i][1])){ //부모노드가 같으면 사이클 -> 다음 간선으로 넘어감
                continue;
            }
             //다르면 union
                union(arr[i][0],arr[i][1]);
                last = arr[i][2];
                price+= last;

        }

        System.out.println(price - last);


    }

    static int find(int a){ //부모가 자기자신이 될때가지 재귀 -> 부모 찾기
        if(parents[a] != a){
            parents[a] = find(parents[a]);
        }
        return parents[a];
    }
    static void union(int a,int b){
        int parentA = find(a); // 노드 a,b 의 부모찾기
        int parentB = find(b);

        if(parentA < parentB){
            parents[parentB] = parentA; // 부모 크고 작음에 따라 부모 바꿔주기
        }
        else{
            parents[parentA] = parentB;
        }
    }
}

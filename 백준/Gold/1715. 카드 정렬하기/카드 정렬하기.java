import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N ;

    static int result = 0;

    static PriorityQueue<Integer> qu = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(bf.readLine().trim());

        for(int i =0; i<N; i++){
            int num = Integer.parseInt(bf.readLine().trim());
            qu.add(num);
        }

        //오름차순 정렬하고 큐에 더해진 애들을 계속 넣자.

        while (qu.size()>1){
            int ar = qu.poll();
            int ar2 = qu.poll();

            result += (ar+ar2);
            qu.add(ar+ar2);
        }

        System.out.println(result);

    }
}

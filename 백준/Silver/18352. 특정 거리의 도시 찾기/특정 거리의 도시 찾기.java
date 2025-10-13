import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 도시 수
        int m = Integer.parseInt(st.nextToken()); // 도로 수
        int k = Integer.parseInt(st.nextToken()); // 목표 거리
        int x = Integer.parseInt(st.nextToken()); // 시작 도시

        // 인접 리스트
        List<List<Integer>> graph = new ArrayList<>(n + 1);
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b); // 단방향 a -> b
        }

        // 거리 배열 (-1: 미방문)
        int[] dist = new int[n + 1];
        Arrays.fill(dist, -1);

        // BFS
        Queue<Integer> q = new ArrayDeque<>();
        dist[x] = 0;
        q.add(x);

        while (!q.isEmpty()) {
            int cur = q.poll();
            for (int next : graph.get(cur)) {
                if (dist[next] == -1) {
                    dist[next] = dist[cur] + 1;
                    q.add(next);
                }
            }
        }

        // 결과 수집
        List<Integer> ans = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (dist[i] == k) ans.add(i);
        }

        StringBuilder sb = new StringBuilder();
        if (ans.isEmpty()) {
            sb.append(-1).append('\n');
        } else {
            Collections.sort(ans);
            for (int v : ans) sb.append(v).append('\n');
        }

        System.out.print(sb.toString());
    }
}

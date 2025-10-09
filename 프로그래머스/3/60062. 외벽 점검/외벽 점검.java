class Solution {
    static int[][] weak_cases;
    boolean[] dist_visit; 
    int[] dist_case;
    int[] dist; 
    int answer;
    public int solution(int n, int[] weak, int[] dist) {
        weak_cases = new int[weak.length][weak.length];
        answer = dist.length +1;
        dist_visit = new boolean[dist.length]; 
        dist_case  = new int[dist.length]; 
        int idx = 0;
        this.dist = dist; 
        makeWeakCase(n,weak,dist);
        distCase(dist_visit,dist_case,idx);
        if(answer == dist.length+1)
            return -1;
        else
            return answer;
    }
    public void makeWeakCase(int n, int[] weak, int[] dist){ //약한벽 케이스 전체 만들기 
        int[] weakCase = weak.clone(); //week 배열 clone
        weak_cases[0] = weakCase.clone(); //0 번째는 기존거 넣어줌
        for(int i =1; i<weak.length; i++){
            int temp = weakCase[0]; //첫번째거 저장해두고 
            for(int j =1; j<weak.length; j++){ //하나씩 밀면서 배열 바꿔줌
                weakCase[j-1] = weakCase[j];
            }
            weakCase[weak.length-1] = n+temp; 
            weak_cases[i] = weakCase.clone(); //바뀐배열 넣어주기 
        }
    };
    
    public void distCase(boolean[] dist_visit, int[] dist_case, int idx){ 
        //왜 순열은 무조건 재귀로 푸는가 .. 
        if(idx == dist_case.length){ //사람 경우의 수 다 만들어 졌으면 
            for(int[] weak_case : weak_cases){ //전체 취약 지점 경우의 수 다 돌리면서 체크
                check(dist_case, weak_case); 
            }
        }
        else{
            for(int i=0; i<dist_case.length; i++){ //전체 dist 돌면서 
                if(!dist_visit[i]){ //방문 확인하고 방문된거면 넣고 재귀-> 빼고 index -- 
                    dist_visit[i] = true; 
                    dist_case[idx] = dist[i]; 
                    distCase(dist_visit,dist_case,idx+1);
                        // idx ++ 미리하면 call stack 에서 빠져서 다시 복구 
                        // idx-- 시켜줘야함. 이전으로 자동으로 안돌아감. 
                    dist_visit[i] = false;
                    dist_case[idx] = 0;
                }
            }
        }
        
    }
    public void check(int[] dist_case, int [] weak_case){
        int cur = 0; //현재 week 인덱스 
        int next; 
        int dist_idx = 0; //거리 인덱스 
        while(cur < weak_case.length && dist_idx < dist_case.length){
            next = cur+1;
            while(next < weak_case.length && weak_case[cur]+dist_case[dist_idx]                 >= weak_case[next]){
                next ++;
                //다음 week 인덱스가 week 길이보다 작고, 현재 위치+길이 한게 
                //다음 week  위치보다 클때 다음 인덱스 위치를 계속 늘려준다. (커버가능)
            }
            cur = next;
            dist_idx++; //while 문 안까지는 하나의 거리를 쓴거니까 인덱스 늘릴필요 없다. 
        }
         if(cur == weak_case.length && dist_idx < answer) 
             //cur <week_case 보다 작으면 걍 넣으면 안되고
             //dist_idx >= answer 이면 기존 answer 보다 크니까 update x 
            answer = dist_idx;
    }
}
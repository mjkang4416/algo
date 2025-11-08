import java.util.*;

class Solution {
    static int[] stage;  
    static int[] stagePeopleNum; //각 스테이지 머무른 사람 수 
    static int[] challange; //각 스테이지 도전자 수 
    static List<Stage> resultStage = new ArrayList<>(); 
    
    class Stage{
        int stage;
        double failPerc; 
        
        public Stage(int stage,double failPerc){
            this.stage = stage;
            this.failPerc = failPerc; 
        }
    }
    
    public int[] solution(int N, int[] stages) {
        //N : 전체 스테이지 개수 
        //stages : 사용자가 현재 멈춰있는 스테이지 번호 -->,N+1(N번째 스테이지)은 마지막 까지 클리어한 사용자 나타냄 
        //실패율 : 스테이지에 도달했으나 , 아직 클리어 못한 플레이어수 /스테이지 도달 플레이어수
        
        stage = stages; 
        
        Arrays.sort(stage); //오름차순 정렬 
        
        stagePeopleNum = new int[N]; //각 스테이지 머무는 사람수 
        challange = new int[N]; //각 스테이지 도전자 수 
        
        //각 스테이지 만큼 돈다. 
        for(int i =0; i<N; i++){
            int result = bfs(0,stage.length-1,i+1); //스테이지 도전 한 사람 수만큼 binarySearch
            stagePeopleNum[i] = result; 
        }
        
        //각 스테이지 도전자 수 게산 
        challange(N); 
        
        
        //실패율 계산 -> resultStage 에 넣기 
        for(int i=0; i<N; i++){
            if(stagePeopleNum[i] == 0){
                resultStage.add(new Stage(i+1,0));
            }
            else{
            resultStage.add(new Stage(i+1,
                                      (double)stagePeopleNum[i]/challange[i]));
            }
           
         }
        //내림차순 정렬 -> 같은경우 작은 번호 스테이지 순
        resultStage.sort((o1,o2)-> {
            if(o1.failPerc == o2.failPerc){
                return o1.stage - o2.stage; 
            }   
            return Double.compare(o2.failPerc, o1.failPerc);
        });
        
        return resultStage.stream().mapToInt(o1->o1.stage).toArray();
    }
    
     //클리어 못한 사람수 구하기 
    public int bfs(int start, int end, int target){
        
        int mid = (start+end)/2; 
        
        //탐색 끝낸 경우 
        if(start > end){
            return 0; 
        }
        
        //target 이 mid 와 일치하는 경우 
        if(stage[mid] == target){
            return 1+ bfs(mid+1,end,target) + bfs(start,mid-1,target);
        }
        else if(stage[mid] > target){
             return bfs(start,mid-1,target); 
        }
        else{
              return bfs(mid+1,end,target);
        }
    }
    
    //각 스테이지 도전자 수 계산 
    public void challange(int N ){
        challange[0] = stage.length;
        //각 스테이지 도전자 계산 
        for(int i =1; i<N; i++){ 
            int result = 0; 
            for(int j=0; j<i; j++){ 
               result += stagePeopleNum[j]; 
            }
            challange[i] = stage.length - result; 
        }
    }
}
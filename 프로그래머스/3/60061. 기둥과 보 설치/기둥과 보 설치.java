import java.util.List;
import java.util.ArrayList;

class Solution {
    static List<int[]> answer; //결과 담을 배열
    static boolean [][][] result;  
       
    public int[][] solution(int n, int[][] build_frame) {
        answer = new ArrayList<int[]>(); //결과 담을 배열
        result = new boolean[n+1][n+1][2];  
        
        //build_frame 배열 순회 
        for(int i =0; i< build_frame.length; i++){ 
            int x = build_frame[i][0];
            int y = build_frame[i][1];
            int a = build_frame[i][2];
            int b = build_frame[i][3]; 
            //벽면 벗어나는 경우 넘어감 
            if(x < 0 || y< 0 || x > n || y > n){ continue; } 
            //바닥에 보를 설치하는 경우 넘어감 
            if(y==0 && a == 1 && b == 1){ continue; } 
            
            //삽입일때
            if(b == 1){
                result[y][x][a] = true;
                if(!check(n)){
                    result[y][x][a] = false;
                }
            }
            //삭제일때
            else{
                result[y][x][a] = false;
                  if(!check(n)){
                      result[y][x][a] = true;
                    }
            }
            
        } 
         for(int i =0; i<=n; i++){
                for(int j =0; j<=n; j++){
                    for(int a = 0; a<2; a++){
                        if(result[i][j][a]==true){
                            answer.add(new int[]{j,i,a});
                        }   
                    }
                }
        }
        
        answer.sort((o1,o2)->{
            // x 좌표 기준 오름차순 정렬 
            if(o1[0]!=o2[0]){
                 return o1[0]-o2[0];
            }
            if(o1[1]!=o2[1]){ //x 좌표가 같은경우 y 기준으로 오름차수 정렬 
                return o1[1]-o2[1];
            }
                //x,y 좌표가 같은 경우 기둥이 보보다 앞에 오게 정렬
                return o1[2]-o2[2];
            
             
        });
        
        return answer.toArray(new int[answer.size()][]);
        
    }
    public boolean check(int n){
        for(int y =0; y<=n; y++){
            for(int x =0; x<=n; x++){
                    //기둥인 경우 
                    if(result[y][x][0]){ 
                        boolean isValid = false;
                        //기둥이 바닥인경우 넘어감
                        if(y == 0 ){isValid=true;} 
                        //다른기둥 위일 경우 넘어감
                        if(y>0 && result[y-1][x][0]){isValid=true;} 
                        //보의 한쪽 끝 위 인 경우 넘어감
                        if((x >0 && result[y][x-1][1])
                           || result[y][x][1]){isValid=true;} 
                       
                        if(!isValid) return false;
                    }
                    //보일 경우 
                    if(result[y][x][1]){ 
                        boolean isValid = false;
                        //보의 한쪽 끝이 기둥일 경우 
                        if((y>0 && result[y-1][x][0])||
                           (y>0 && x<n && result[y-1][x+1][0])
                           ){
                            isValid=true;
                        }
                        //보의 양쪽 끝이 다른 보랑 연결 돼 있는 경우 
                        if((x<n && result[y][x+1][1]) && (x>0 && 
                           result[y][x-1][1])){
                            isValid=true;
                        }
                        if(!isValid) return false; 
                    } 
                }
            } 
            return true; 
        }
  }
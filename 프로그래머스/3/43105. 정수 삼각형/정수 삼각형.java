import java.util.*;

class Solution {
    public int solution(int[][] triangle) {
        //아래칸 이동 -> 대각선 방향으로 한칸 ( 오, 왼)
        //거쳐간 숫자의 합이 최대가 되도록 
        int answer = 0;
        
        
        for(int i =1; i<triangle.length; i++){
            for(int j =0; j<triangle[i].length; j++){
                if(j==0){
                    triangle[i][j] += triangle[i-1][j];
                }
                else if(j== triangle[i].length-1){
                    triangle[i][j] += triangle[i-1][j-1];
                }
                else{
                     triangle[i][j] += Math.max(triangle[i-1][j-1] , triangle[i-1][j]);
                }
            }
        }
        
        for(int i =0; i<triangle[triangle.length -1].length-1; i++){
            answer = Math.max(answer,triangle[triangle.length-1][i]);
        }
        
        return answer;
    }
}
class Solution {
    public boolean solution(int[][] key, int[][] lock) {
        boolean answer = true; 
        
        int length = lock.length + 2*key.length -2 ;
        
        int start = key.length-1;
            
        int last = key.length+lock.length-1;
        
        for(int x = 0; x<last; x++){
            for(int y =0; y<last; y++){
            //4번 회전 
                for(int i =0; i<4; i++){
                    //새 배열 만들어서 lock 담기 
                    int[][] newLock = new int[length][length];
                    
                    for(int j=0; j<lock.length; j++){
                        for(int k =0; k<lock.length; k++){
                            newLock[j+start][k+start] = lock[j][k];
                        }
                    }
                    //key 회전
                    rotate(newLock,key,i,x,y);
                    //회전된 key lock 과 확인 
                    if(match(newLock,lock.length,key.length-1)){
                        return answer;
                    }
                    }
                }
            }
            return false;
        }
    

    public void rotate(int[][] newLock,int[][] key, int root, int x, int y){
        for(int i =0; i<key.length; i++){ //돌면서 회전 경우에 따라 newArr 갱신
            for(int j =0; j<key.length; j++){
                if(root == 0){ // 회전 안하는경우 
                    newLock[i+x][j+y] += key[i][j];
                }
                else if(root ==1){ //90도 회전 
                    newLock[i+x][j+y] += key[key.length-1-j][i]; 
                }
                else if(root ==2){
                     newLock[i+x][j+y] += key[key.length-1-i][key.length-1-j]; 
                }
                else{
                    newLock[i+x][j+y] += key[j][key.length-1-i]; 
                }
            }
        }
    }
    
    public boolean match(int[][] newLock, int length, int point){
        for(int i=0; i<length; i++){
            for(int j =0; j<length; j++){
                if(newLock[i+point][j+point] != 1){
                    return false;
                }
            }
        }
        return true;
    }
}

import java.util.LinkedList;
import java.util.Collections;

class Solution {
    
    public int solution(int[] food_times, long k) { //food_time 과 멈추는 시점 입력
        LinkedList<Food> list = new LinkedList<>(); //LinkedList 고유 메서드 쓸거면 인터페이스 타입으로 선언하면 안됨. 
        int len = food_times.length; 
        
        for(int i =0; i<len; i++){ 
            //음식 번호와 숫자가 담긴 객체 음식 순서대로 담기
            list.add(new Food(i+1,food_times[i])); 
        }
        
        Collections.sort(list,(o1,o2)->o1.time-o2.time); //시간 작은거 순으로 sort
        
        int currentTime = 0; // 이전에 뽑힌 노드 시간
        int index = 0; //현재 인덱스 
        
        
        for(Food f: list){
            // 현재 노드 먹는시간 - 이전에 뽑힌 노드 먹는시간
            long diff = f.time - currentTime; 
            if(diff != 0){ //차이가 0이 아니면 
                long spend = diff * len; // 차이 * 전체 배열 개수 
                if(spend <= k){ //k 까지 도달전 
                    k-= spend; //k 에서 먹은 시간 뺌 
                    currentTime = f.time; 
                }
                else{ //이번거 빼면 k 넘음 , 이제 정렬해서 구해야 
                    k%=len; //돌면서 빠진 len 으로 나눈 나머지
                    list.subList(index,food_times.length)
                        .sort((o1,o2)->o1.num-o2.num); //num 으로 정렬
                        return list.get(index+(int)k).num ;//현재에서 k 만큼 더 간거 
                    
                }
            }
            index++; //하나가 linkedList 에서 뽑혀서 처리되면 index ++ , 전체 길이는 준다.
            len--; 
        }
        return -1;
    }
}

class Food{
    int num, time;
    
    public Food(int num, int time){
        this.num = num; 
        this.time = time; 
    }
    
}

/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.*; 
import java.io.*; 

public class Main
{
    static int T,n; 
    static char com[]; 
    static String arr[]; 
    
    
	public static void main(String[] args) throws IOException{
		
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(bf.readLine()); 
		
		for(int t=0; t<T; t++){
		    com = bf.readLine().toCharArray();
		    n = Integer.parseInt(bf.readLine()); 
		  
		    arr = bf.readLine().replace("[","").replace("]","").split(","); 
		    Deque<String> q = new ArrayDeque<>(); 
		    
		    for(int i=0; i<n; i++){
		        q.add(arr[i]); 
		    }
		    
		    //명령실행
		    boolean isok = true;
		    boolean isR = false;
		    for(int i=0; i<com.length; i++){
		        if(com[i]=='R'){ //뒤집기
		            if(isR){
		                isR = false;
		            }else{
		                isR = true;
		            }
		        }else { //삭제하기 
		            if(q.size()>0){
		                if(isR){ //뒤집어 진 경우 
		                  q.pollLast(); 
		                }else{
		                  q.pollFirst(); 
		                }
		            }else{
		                isok = false; 
		                break;
		            }
		        }
		    }
		    if(isok){
		        List<String> result = new ArrayList<>(q); 
		        if (result.size() == 0) {
                    System.out.println("[]");
                    continue;
                }
		        if(!isR){ //뒤집어지지 않은 경우 
    		        System.out.print("[");
    		        for(int i=0; i<result.size()-1; i++){ //큐 빼면 계속 사이즈 줄어든다 .. 
    		            System.out.print(result.get(i)+",");
    		        }
    		        System.out.print(result.get(result.size()-1));
    		        System.out.print("]");
    		        System.out.println(); 
		        }else{
		            System.out.print("[");
    		        for(int i=result.size()-1; i>0; i--){
    		            System.out.print(result.get(i)+",");
    		        }
    		        System.out.print(result.get(0));
    		        System.out.print("]");
    		        System.out.println(); 
		        }
		        
		    }else{
		        System.out.println("error"); 
		    }
		}
	    
	    
	    
	}
	
}
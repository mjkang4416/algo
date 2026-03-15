/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.*; 
import java.io.*; 

public class Main
{
    static int[][] arr; 
    static int n,m,result; 
    static List<int[]> chiken; 
    static List<int[]> house; 
    
	public static void main(String[] args) throws IOException{
		//치킨집 조합 m 개 만들고 치킨거리가 가장 작은거 선택
		
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine()); 
		
		//배열 받아오기 
		n = Integer.parseInt(st.nextToken()); 
		m = Integer.parseInt(st.nextToken()); 
		arr = new int[n][n];
		house = new ArrayList<>();
		chiken = new ArrayList<>(); 
		result = 1000000000;
		
		for(int i=0; i<n; i++){
		    st = new StringTokenizer(bf.readLine()); 
		    for(int j=0; j<n; j++){
		        arr[i][j] = Integer.parseInt(st.nextToken()); 
		        if( arr[i][j] ==1){
		            house.add(new int[]{i,j});
		        }
		        if(arr[i][j] ==2){
		            chiken.add(new int[]{i,j});
		        }
		    }
		}
		
		//치킨집 조합 구하기 
		combi(0,0,new int[m][2]);
		
		
		System.out.println(result); 
	
	}
	
	static void combi(int start,int cnt,int[][]temp){
	    if(cnt==m){
	        //치킨거리 구하기 
	        sum(temp); 
	        return ;
	    }
	    
	    for(int i=start; i<chiken.size(); i++){
	        int[] now = chiken.get(i);
 	        temp[cnt][0] = now[0];
 	        temp[cnt][1] = now[1]; 
 	        combi(i+1,cnt+1,temp); 
	    }
	}
	
	static void sum(int[][] temp){
	    int answer = 0; 
	    
	    for(int[] h : house){
	        int x = h[0];
	        int y = h[1]; 
	        int houseSum = 1000000000;
	        for(int[] c : temp){
	            int sum = Math.abs(c[0]-x)+Math.abs(c[1]-y); 
	            houseSum = Math.min(houseSum,sum); 
	        }
	        answer+= houseSum;
	    }
	    result = Math.min(result,answer); 
	}
	
}
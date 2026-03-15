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
    static List<int[]> zero; 
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    
	public static void main(String[] args) throws IOException{
		//벽 3개 세운 뒤 안전영역의 크기를 구해야 함
		
		//배열 만들기
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine()); 
		
		n = Integer.parseInt(st.nextToken()); 
		m = Integer.parseInt(st.nextToken()); 
		zero = new ArrayList<>(); 
		arr = new int[n][m]; 
		result =0; 
		
		
		
		for(int i=0; i<n; i++){
		    st = new StringTokenizer(bf.readLine());
		    for(int j=0; j<m; j++){
		        arr[i][j] = Integer.parseInt(st.nextToken()); 
		         //0인 좌표구하기
		        if(arr[i][j]==0){
		            zero.add(new int[]{i,j}); 
		        }
		    }
		}
		
		//벽 세울 수 있는 경우의 수 구하기
	    combi(0,0); 
		    
		System.out.println(result); 
	}

	public static void combi(int start,int cnt){
	    if(cnt==3){
	        //안전영역의 크기 구하기 
	        bfs();
	        return ;
	    }
	    
	    for(int i=start; i<zero.size(); i++){
	        int[] now = zero.get(i); 
	        int a = now[0];
	        int b = now[1]; 
	        arr[a][b] = 1;
	        combi(i+1,cnt+1); 
	        arr[a][b] = 0; 
	    }
	}
	
	public static void bfs(){
	    Deque<int[]> q = new ArrayDeque<>();
	    for(int i=0; i<n; i++){
	        for(int j=0; j<m; j++){
	            if(arr[i][j]==2){
	                q.add(new int[]{i,j}); 
	            }
	        }
	    }
	    int[][] copyArr = new int[n][m];
	    for(int i=0; i<n; i++){
	        copyArr[i] = arr[i].clone(); 
	    }
	    
	    while(!q.isEmpty()){
	        int[] now = q.poll(); 
	        int x = now[0];
	        int y = now[1]; 
	        
	        for(int i=0; i<4; i++){
	            int nx = x+dx[i]; 
	            int ny = y+dy[i];
	            if(nx>=0 && nx<n && ny>=0 && ny<m && copyArr[nx][ny]==0){
	                copyArr[nx][ny]=2;
	                q.add(new int[]{nx,ny}); 
	            }
	        }
	    }
	    
	    cntzero(copyArr); 
	}
	
	public static void cntzero(int[][] copyArr){
	    int cnt=0; 
	    for(int i=0; i<n; i++){
	        for(int j=0; j<m; j++){
	            if(copyArr[i][j]==0){
	                cnt++; 
	            }
	        }
	    }
	    result = Math.max(result,cnt); 
	}
}
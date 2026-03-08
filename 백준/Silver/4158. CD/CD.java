/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.*;
import java.io.*;
public class Main
{
    static int n,m,answer,result,idx,point1,point2;
    static int arr1[],arr2[]; 
    
	public static void main(String[] args) throws IOException{
	   BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	   while(true){
    	   StringTokenizer st = new StringTokenizer(bf.readLine()); 
    	   n = Integer.parseInt(st.nextToken());  //n 을 몇개의 연속된 자연수로 나타낼 수 있는지
    	   m = Integer.parseInt(st.nextToken());
    	   if(n==0 && m==0){
    	       break;
    	   }
    	   arr1 = new int[n]; 
    	   arr2 = new int[m]; 
    	   idx=0;
    	   point1=0; 
    	   point2=0; 
    	   result=0; 
    	   
    	   for(int i=0; i<n; i++){
    	     arr1[i] = Integer.parseInt(bf.readLine());  //동시에 가지고 있는 cd 수 
    	   }
    	   
    	   for(int i=0; i<m; i++){
    	     arr2[i] = Integer.parseInt(bf.readLine());  
    	   }
    	   
    	   while(true){
    	       if(point2 == m || point1 == n){
    	           break;
    	       }
    	       
    	       if(arr1[point1]==arr2[point2]){
    	           point1++;
    	           point2++; 
    	           result++;
    	       }else if(arr1[point1]<arr2[point2]){point1++;}
    	       else{point2++;} 
    	       
    	   }
    	  
    	   System.out.println(result); 
	   }
	}

}

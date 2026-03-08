/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.*;
import java.io.*;
public class Main
{
    static int n,m,answer,start,end,result;
    static int arr[]; 
    
	public static void main(String[] args) throws IOException{
	   BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	   n = Integer.parseInt(bf.readLine());  //n 을 몇개의 연속된 자연수로 나타낼 수 있는지
	   arr = new int[n]; 
	   start = 0; 
	   end=0; 
	   answer=0;
	   result=0;
	   for(int i=0; i<n; i++){
	       arr[i] = i+1; 
	   }

	   for(int i=0; i<n; i++){
	        result+=arr[i];
            while(result>n){
                result-=arr[start++];
            }
                  
           if(result==n){
    	       answer++; 
           }
	     
	   }
	   System.out.println(answer);
	    
	}

}

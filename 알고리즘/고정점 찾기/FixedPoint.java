import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class FixedPoint {
    static int N ;
    static int [] arr;

    static int result;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(bf.readLine());

        arr = new int [N];
        for(int i =0; i<N; i++){
            arr[i]= Integer.parseInt(st.nextToken());
        }
        binarySearch(0,N-1);

        if(result==0){
            System.out.println(-1);
        }
        else{
            System.out.println(result);
        }
    }
    public static void  binarySearch(int start, int end){
        int mid = ( start + end )/2;

        if(start > end){
            return;
        }
        if(mid == arr[mid]){
            result = mid;
            binarySearch(start,mid-1);
            binarySearch(mid+1,end);
        }
        else if( mid < arr[mid] ){
            binarySearch(start,mid-1);
        }
        else{
            binarySearch(mid+1,end);
        }
    }
}

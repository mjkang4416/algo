import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class CountNumberInSortedArray {
    static int N;
    static int x;

    static int cnt = 0;

    static int [] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        arr = new int[N];

        st = new StringTokenizer(bf.readLine());

        for(int i =0; i<N; i++){
            arr[i]= Integer.parseInt(st.nextToken());
        }

        binarySearch(0,N-1);

        if(cnt == 0){
            System.out.println(-1);
        }
        else{
            System.out.println(cnt);
        }

    }

    public static void binarySearch(int start, int end){
        if(start > end){
            return;
        }
        int mid = ( start + end ) / 2;
        if(arr[mid] == x){
            cnt++;
            binarySearch(mid+1,end);
            binarySearch(start,mid-1);
        }
        else if(arr[mid] > x){
            binarySearch(start,mid-1);
        }
        else{
            binarySearch(mid+1,end);
        }
    }
}

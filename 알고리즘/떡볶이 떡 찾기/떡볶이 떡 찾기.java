
import java.util.Arrays;
import java.util.Scanner;

public class MakingTeokbokki {

    static int N;
    static int M;
    static int[] Teok;
    static int[] servedTeok;

    static int result;


    public static int binary_search(int start, int end, int target){
        if(start>end){
            return 0;
        }
        int mid = (start+end)/2;
        for(int i=0; i<N; i++){ //mid 를 target 으로 잡고 자른떡 servedTeok 에 넣음
            if(Teok[i]-Teok[mid]>=0) {
                servedTeok[i] = Teok[i] - Teok[mid];
            }
            else{
                servedTeok[i] = 0;
            }
        }
        for(int j = 0; j<N; j++){ //자른떡 result 계산
            result += servedTeok[j];
        }

        if(result == target){
            return Teok[mid];
        }
        else if (result < target) {
            return binary_search(start,mid-1,target);
        }
        else{
            return binary_search(mid+1,end,target);
        }

    }

    public static void main(String[] args) {
        //각자 다른 N 개의 떡 중 길이에서  H 를 뺀 것만 소비자가 가져감
        //소비자가 가져가느 떡의 길이 M 이 주어진 값과 일정하게 만들어야

        Scanner sc = new Scanner(System.in);
        N  = sc.nextInt();
        M = sc.nextInt();
        Teok = new int[N];
        servedTeok = new int[N];
        result =0;

        for(int i =0; i<N; i++){
            Teok[i] = sc.nextInt();
        }

        Arrays.sort(Teok);

        System.out.println(binary_search(0,N-1,M));

    }
}

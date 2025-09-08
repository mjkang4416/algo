import java.util.Scanner;

public class MakingXTo1 {
    public static void main(String[] args) {
        //x 가 5,3,2 로 나누어 떨어지면 해당 숫자로 나눈다
        //x 에서 1을 뺀다
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int[] d = new int[x+1]; //메모라이즈 할 배열, 자바는 자동으로 0 으로 초기화됨

        for(int i =2; i<x+1; i++){
            //1 빼는 경우
            d[i] = d[i-1]+1;
            //2로 나누어 떨어지는 경우
            if(i%2==0){
                d[i] = Math.min(d[i],d[i/2]+1);
            }
            //3으로 나누어 떨어지는 경우
            if(i%3==0){
                d[i] = Math.min(d[i],d[i/3]+1);
            }
            //5로 나누어 떨어지는 경우
            if(i%5==0){
                d[i] = Math.min(d[i],d[i/5]+1);
            }
        }
        System.out.println(d[x]);
    }
}

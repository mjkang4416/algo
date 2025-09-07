import java.util.Scanner;

public class RoyalKnight {
    public static void main(String[] args) {
        // 8*8 체스판 위에 말이 있다.
        // 나이트의 위치가 주어졌을때 이동할 수 있는 경우의 수는 ?
        // 가로가로 세로, 세로세로 가로 로만 이동 가능
        // 밖으로 나갈 수 없다.
        // 직사각형의 중심에 있을때 젤 많이 이동 가능

        Scanner sc = new Scanner(System.in);


        String stop = sc.next();
        int first = stop.charAt(0)-97; //x
        int second = stop.charAt(1)-'0'-1; //y

        int count = 0;

        int[][] stepList = {{1,-2},{2,-1},{-1,-2},{-2,-1},{2,1},{1,2},{-2,1},{-1,2}}; //가능한 조합들

        for(int i = 0; i<8; i++){
            int newFirst = first+stepList[i][0];
            int newSecond = second+stepList[i][1];

            if(newFirst <0 || newSecond<0 || newFirst>7 || newSecond > 7){
                continue;
            }
            count ++;
        }

        System.out.println(count);
    }
}

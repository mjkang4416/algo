import java.util.Scanner;

public class LowScores {
    public static void main(String[] args) {
        //학생의 이름과 성적이 주어졌을때 성적이 낮은 순서대로 학생 이름 출력 (오른차순)

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        String[][] score = new String[N][2];
        String[] resultName = new String[N];

        for(int i = 0; i<N; i++){
            score[i][0] = sc.next();
            score[i][1] = sc.next();
        }



        for(int j = 0; j<N-1; j++){
            for(int q = j+1; q<N; q++){
                int ord = Integer.parseInt(score[j][1]);
                int newScore = Integer.parseInt(score[q][1]);
                if(ord > newScore){
                    String temp = score[j][0];
                    resultName[j] = score[q][0];
                    resultName[q] = temp;
                }
            }
        }

        for(int i =0; i<N; i++){
            System.out.println(resultName[i]);
        }
    }
}

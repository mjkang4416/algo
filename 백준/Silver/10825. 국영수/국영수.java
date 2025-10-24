import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int N = Integer.parseInt(st.nextToken());

        List<Student> studentsArr = new ArrayList<>();

        for(int i =0; i<N; i++){
            st = new StringTokenizer(bf.readLine());
            String name = st.nextToken();
            int k = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());

            studentsArr.add(new Student(name,k,y,s));
        }


        studentsArr.sort((o1, o2)-> {
            //국어 점수가 감소하는 순서로
            if(o2.k != o1.k ) return o2.k - o1.k;
            //국어 점수가 같으면 영어 점수가 증가하는 순서로
            if(o2.y != o1.y ) return o1.y - o2.y;
            //국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
            if (o1.s != o2.s) return o2.s - o1.s;
            return o1.name.compareTo(o2.name);
            //모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로
        });

        for(int i =0; i<N; i++){
            System.out.println(studentsArr.get(i).name);
        }
    }

    static class Student{
        String name;
        int k;
        int y;
        int s;
        Student(String name, int k, int y,int s){
            this.name = name;
            this.k = k;
            this.y = y;
            this.s = s;
        }
    }
}

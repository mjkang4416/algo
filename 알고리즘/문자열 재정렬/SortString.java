import java.util.*;

public class SortString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String S = sc.next();

        ArrayList<Character> arr = new ArrayList<>();
        int num = 0;

        for(int i =0; i<S.length(); i++){
            if(Character.isDigit(S.charAt(i))){
                num+= S.charAt(i)-'0';
            }
            else{
                arr.add(S.charAt(i));
            }
        }

        Collections.sort(arr);

        for(int i =0; i<arr.size(); i++){
            System.out.print(arr.get(i));
        }

        System.out.print(num);

    }
}

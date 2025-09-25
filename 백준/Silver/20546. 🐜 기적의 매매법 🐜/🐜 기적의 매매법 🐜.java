import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int money = Integer.parseInt(br.readLine().trim());
        int[] StockPrice = new int[14];


        StringTokenizer st = new StringTokenizer(br.readLine()); // 공백 단위로 14개 읽기
        for (int i = 0; i < 14; i++) {
            StockPrice[i] = Integer.parseInt(st.nextToken());
        }

        int j = bnp(StockPrice,money);
        int s = threeTree(StockPrice,money);

        if(j>s){
            System.out.println("BNP");
        }
        else if(j<s){
            System.out.println("TIMING");
        }
        else{
            System.out.println("SAMESAME");
        }
    }


    public static int bnp(int[]StockPrice, int money){
        int remain = money;
        int myStockNum =0;
        for(int i =0; i<StockPrice.length; i++){
            if(remain < StockPrice[i]){
                continue;
            }
            if(StockPrice[i]!=0){
                myStockNum += remain/StockPrice[i];
                remain %= StockPrice[i];
            }
        }
        return remain + myStockNum*StockPrice[13];
    }

    public static int threeTree(int[]StockPrice, int money){
        int remain = money;
        int myStockNum =0;
        int upCount = 0;
        int downCount = 0;

        for(int i =0; i<StockPrice.length-1; i++){

            //3일 연속 상승-> 다음거 전량 매도
            if(upCount==3) {
                upCount = 0;
                downCount = 0;

                remain += StockPrice[i]*myStockNum;
                myStockNum = 0 ;
            }

            else if(downCount == 3 && StockPrice[i]!=0){ //3일 연속 하락 -> 다음거 전량 매수

                downCount = 0;
                upCount = 0;

                //살 돈 없으면 다음거
                if(remain < StockPrice[i]){
                    continue;
                }

                myStockNum += remain/StockPrice[i];
                remain %= StockPrice[i];
            }

            //다음 노드가 이전 노드보다 크고 작은지 판단
            if(StockPrice[i]<StockPrice[i+1]){
                upCount++;
                downCount = 0;
            }
            else if(StockPrice[i]>StockPrice[i+1]){
                downCount ++;
                upCount = 0;
            }

        }
        return remain + myStockNum*StockPrice[13];
    }
}
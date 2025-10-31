import java.util.*;

class Solution {
    class Trie{
        Map<Integer,Integer> lenMap = new HashMap<>(); 
        Trie[] child = new Trie[26]; 
        
        //word 전체 삽입 
        void insert(String str){
            Trie node = this; //이거따라 front 랑 back 
            int len = str.length(); //현재 문자열 길이 
            lenMap.put(len,lenMap.getOrDefault(len,0)+1); //해시맵 이용해서 값 누적
            
            for(char ch : str.toCharArray()){
                int idx = ch-'a'; 
                if(node.child[idx]==null){ //해당 자식이 없으면
                    node.child[idx] = new Trie(); //자식 노드 만들어주고 
                }
                node = node.child[idx]; //현재 노드 바꿔줌
                node.lenMap.put(len, node.lenMap.getOrDefault(len, 0) + 1); //이전거 +1; 
            }
        }
        int find(String st, int i){
            if(st.charAt(i)=='?'){ 
                return lenMap.getOrDefault(st.length(),0);
            }
            int idx = st.charAt(i)-'a';
            return child[idx] == null ? 0 : child[idx].find(st, i + 1);
        }
    }
    public int[] solution(String[] words, String[] queries) {
        int[] answer = {};
        Trie front = new Trie();
        Trie back = new Trie();
        
        for(String word : words){ //어짜피 하나의 트리에 모든 word 담을것 
            front.insert(word); //순방향 트리, 역방향 트리 
            back.insert(reverse(word));
        }
        
        return Arrays.stream(queries) //queries 하나씩 가져와서 순방향, 역방향 정함
            .mapToInt(query->query.charAt(0)=='?'? back.find(reverse(query),0): front.find(query,0)).toArray();
    }
    
    String reverse(String words){ 
        return new StringBuilder(words).reverse().toString();
    }
}
import java.util.*;

class Solution {
    ArrayList<String> dict = new ArrayList<>();
    String[] vowel = {"A", "E", "I", "O", "U"};
    
    public int solution(String word) {
        int answer = 0;
        dfs("", 0);
        
        for(int i = 0; i < dict.size(); i++) {
            if (dict.get(i).equals(word)) {
                System.out.println(i);
                answer = i;
                break;
            }
        }
        
        return answer;
    }
    
    void dfs(String str, int len) {
        dict.add(str);
        if (len == 5) return;
        for (int i = 0; i < vowel.length; i++) {
            dfs(str + vowel[i], len+1);
        }
    }
}
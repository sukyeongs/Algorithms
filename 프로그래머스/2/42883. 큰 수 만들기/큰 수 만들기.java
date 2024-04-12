import java.util.*;

class Solution {
    public String solution(String number, int k) {
        StringBuilder answer = new StringBuilder("");
        int start = 0;
        int len = number.length() - k;
        
        while (start < number.length() && answer.length() != len) {
            int max = 0;
            int leftNum = k + answer.length() + 1;
            for(int i = start; i < leftNum; i++) {
                if (max < number.charAt(i) - '0') {
                    max = number.charAt(i) - '0';
                    start = i + 1;
                }
            }
            answer.append(max);
        }
        
        return answer.toString();
    }
}
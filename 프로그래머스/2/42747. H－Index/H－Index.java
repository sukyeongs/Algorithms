import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        int n = citations.length;
        
        for(int i = 0; i < n; i++) {
            int smaller = Math.min(citations[i], n - i);
            answer = Math.max(answer, smaller);
        }
        
        return answer;
    }
}
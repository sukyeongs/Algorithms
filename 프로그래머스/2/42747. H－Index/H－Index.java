import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        int n = citations.length;
        
        for(int h = 0; h < n; h++) {
            int hIndex = n - h;
            if (citations[h] >= hIndex) {
                answer = hIndex;
                break;
            }
        }
        
        return answer;
    }
}
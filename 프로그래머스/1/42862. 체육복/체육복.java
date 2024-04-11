import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n;
        int[] gymSuit = new int[n];
        
        for(int num: lost) gymSuit[num-1]--;
        for(int num: reserve) gymSuit[num-1]++;
        
        for(int i = 0; i < n; i++) {
            if(gymSuit[i] == -1) {
                if(i-1 >= 0 && gymSuit[i-1] == 1) {
                    gymSuit[i-1]--;
                    gymSuit[i]++;
                } else if (i+1 < n && gymSuit[i+1] == 1) {
                    gymSuit[i+1]--;
                    gymSuit[i]++;
                } else {
                    answer--;
                }
            }
        }
        
        return answer;
    }
}
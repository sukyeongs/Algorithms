import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int i=0; i<commands.length; i++) {
            int start = commands[i][0];
            int end = commands[i][1];
            int target = commands[i][2];
            int[] newArray = Arrays.copyOfRange(array, start-1, end);
            Arrays.sort(newArray);
            answer[i] = newArray[target-1];
        }
        
        return answer;
    }
}
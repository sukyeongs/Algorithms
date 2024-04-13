import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        Queue<Integer> progressQueue = new LinkedList<>();
        Queue<Integer> speedQueue = new LinkedList<>();
        
        for(int progress: progresses) progressQueue.add(progress);
        for(int speed: speeds) speedQueue.add(speed);
        
        int day = 0;
        int cnt = 0;
        while(!progressQueue.isEmpty()) {
            if (progressQueue.peek() + day * speedQueue.peek() >= 100) {
                progressQueue.remove();
                speedQueue.remove();
                cnt++;
            } else {
                if (cnt != 0) {
                    answer.add(cnt);
                    day++;
                    cnt = 0;
                } else {
                    day++;
                }
            }
        }
        
        answer.add(cnt);
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
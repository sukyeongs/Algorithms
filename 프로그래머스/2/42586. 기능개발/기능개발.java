import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        Queue<Integer> progressQueue = new LinkedList<>();
        Queue<Integer> speedQueue = new LinkedList<>();
        
        for (int progress : progresses) progressQueue.add(progress);
        for (int speed : speeds) speedQueue.add(speed);
        
        int cnt = 0;
        int day = 0;
        
        while (!progressQueue.isEmpty()) {
            if (progressQueue.peek() + speedQueue.peek() * day >= 100) {
                cnt ++;
                progressQueue.remove();
                speedQueue.remove();
            } else {
                if (cnt > 0) {
                    answer.add(cnt);
                    cnt = 0;
                }
                day++;
            }
        }
        
        answer.add(cnt);
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
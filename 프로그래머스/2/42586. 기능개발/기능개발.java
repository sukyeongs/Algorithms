import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        Queue<Integer> progress = new LinkedList<>();
        Queue<Integer> speed = new LinkedList<>();
        
        for(int i = 0; i < progresses.length; i++) {
            progress.add(progresses[i]);
            speed.add(speeds[i]);
        }
        
        int cnt = 0;
        int day = 0;
        while (!progress.isEmpty()) {
            if(progress.peek() + day * speed.peek() >= 100) {
                progress.remove();
                speed.remove();
                cnt++;
            } else {
                if (cnt != 0) { 
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
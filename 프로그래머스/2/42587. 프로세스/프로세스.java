import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < priorities.length; i++) {
            queue.add(new int[] {priorities[i], i});
        }
        
        while(true) {
            int[] cur = queue.remove();
            int priority = cur[0];
            int index = cur[1];
            boolean firstFlag = true;
            
            for (int[] element: queue) {
                if (element[0] > priority) {
                    queue.add(new int[] {priority, index});
                    firstFlag = false;
                    break;
                }
            }
            
            if (firstFlag) {
                answer++;
                if (index == location) return answer;
            }
            
        }

    }
}
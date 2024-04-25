import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int time = 0;
        Queue<Integer> queue = new LinkedList<>();
        for(int tw : truck_weights) queue.add(tw);
        Queue<Integer> bridge = new LinkedList<>();
        for(int i = 0; i < bridge_length; i++) bridge.add(0);
        
        int currentWeight = 0;
        while (!queue.isEmpty()) {
            time++;
            currentWeight -= bridge.remove();
            
            if (currentWeight + queue.peek() <= weight) {
                currentWeight += queue.peek();
                bridge.add(queue.remove());
            } else {
                bridge.add(0);
            }
        }
        
        return time + bridge_length;
    }
}
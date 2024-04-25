import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        
        for(int s : scoville) heap.add(s);

        while (!heap.isEmpty()) {
            if (heap.peek() >= K) break;
            if (heap.size() == 1 && heap.peek() < K) {
                answer = -1;
                break;
            }
            int mix = heap.remove() + heap.remove() * 2;
            heap.add(mix);
            answer++;
        }
        
        return answer;
    }
}
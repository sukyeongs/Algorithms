import java.util.Stack;

class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        
        for(int i = 0; i < n; i++) {
            answer[i] = n - i - 1;
        }
        
        Stack<Integer> stack = new Stack<>();
        stack.push(0);
        for(int i = 1; i < n; i++) {
            while (!stack.empty() && prices[stack.peek()] > prices[i]) {
                int j = stack.pop();
                answer[j] = i - j;
            }
            stack.push(i);
        }
        
        return answer;
    }
}
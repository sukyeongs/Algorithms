class Solution {
    int answer = 0;
    boolean[] visited;
    
    public int solution(String begin, String target, String[] words) {
        visited = new boolean[words.length];
        dfs(words, begin, target, 0);
        return answer;
    }
    
    void dfs(String[] words, String cur, String target, int depth) {
        if (cur.equals(target)) {
            answer = depth;
            return;
        }
        
        if (depth == words.length && cur != target) {
            answer = 0;
            return;
        }
        
        for (int i = 0; i < words.length; i++) {
            if (!visited[i] && calcDiff(cur, words[i]) == 1) {
                visited[i] = true;
                dfs(words, words[i], target, depth + 1);
                visited[i] = false;
            }
        }
    }
    
    int calcDiff(String cur, String target) {
        int count = 0;
        for (int i = 0; i < target.length(); i++) {
            if (cur.charAt(i) != target.charAt(i)) count++;
        }
        return count;
    }
}
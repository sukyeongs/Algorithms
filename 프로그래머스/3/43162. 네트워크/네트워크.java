import java.util.*;

class Solution {
    ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    boolean[] visited;
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        
        for(int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(i != j && computers[i][j] == 1) {
                    graph.get(i).add(j);
                }
            }
        }
        
        for(int i = 0; i < n; i++) {
            if(visited[i] == false) {
                answer++;
                dfs(i);
            }
        }

        return answer;
    }
    
    void dfs(int cur) {
        visited[cur] = true;
        for(Integer node: graph.get(cur)) {
            if(visited[node] == false) {
                dfs(node);
            }
        }
    }
}
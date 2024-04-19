import java.util.*;

class Solution {
    ArrayList<Integer>[] graph;
    boolean[] visited;
    public int solution(int n, int[][] computers) {
        int answer = 0;
        graph = new ArrayList[n];
        visited = new boolean[n];
        
        for(int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(computers[i][j] == 1 && i != j) {
                    graph[i].add(j);
                }
            }
        }
        
        for(int i = 0; i < n; i++) {
            if(!visited[i]) {
                answer++;
                dfs(i);
            }
        }
        
        return answer;
    }
    
    void dfs(int cur) {
        visited[cur] = true;
        for(Integer node: graph[cur]) {
            if(!visited[node]) {
                visited[node] = true;
                dfs(node);
            }
        }
    }
}
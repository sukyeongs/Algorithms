import java.util.*;

class Solution {
    int[] dx = {1, 0, -1, 0};
    int[] dy = {0, 1, 0, -1};
    
    public int solution(int[][] maps) {
        int answer = bfs(maps, 0, 0);
        if(answer == 0) return -1;
        return answer+1;
    }
    public int bfs(int[][] maps, int x, int y) {
        int[][] visited = new int[maps.length][maps[0].length];
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {x, y});
        
        while(!queue.isEmpty()) {
            int[] current = queue.remove();
            int c = current[0];
            int r = current[1];
            for(int i = 0; i < 4; i++) {
                int nc = c + dx[i];
                int nr = r + dy[i];
                if(nc >= 0 && nc < maps.length && nr >= 0 && nr < maps[0].length) {
                    if(maps[nc][nr] != 0 && visited[nc][nr] == 0) {
                        queue.add(new int[] {nc, nr});
                        visited[nc][nr] = visited[c][r] + 1;
                    }
                }
            }
        }
        
        return visited[maps.length-1][maps[0].length-1];
    }
}
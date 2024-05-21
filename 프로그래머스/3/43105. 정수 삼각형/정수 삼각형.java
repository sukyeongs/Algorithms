class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int floor = triangle.length - 1;
        
        while (floor > 0) {
            for(int i = 0; i < floor; i++) {
                triangle[floor-1][i] += Math.max(triangle[floor][i], triangle[floor][i+1]);
            }
            floor--;
        }

        return triangle[0][0];
    }
}
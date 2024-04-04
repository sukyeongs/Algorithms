class Solution {
    public int solution(int[][] sizes) {
        int height = 0, width = 0;
        for (int[] size : sizes) {
            height = Math.max(height, Math.max(size[0], size[1]));
            width = Math.max(width, Math.min(size[0], size[1]));
        }
        return height * width;
    }
}
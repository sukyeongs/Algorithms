class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        for (int height = 1; height < brown/2; height++) {
            int width = brown/2 - height;
            if (width < height + 2) break;
            
            if (width * (height + 2) - brown == yellow) {
                answer[0] = width;
                answer[1] = height + 2;
            }
        }
        
        return answer;
    }
}
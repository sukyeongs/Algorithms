class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        
        String[] dict = {"aya", "ye", "woo", "ma"};
        
        for (String str: babbling) {
            for (String check: dict) {
                str = str.replace(check, " ");
            }
            if (str.replaceAll(" ", "").equals("")) {
                answer++;
            }
        }
        
        return answer;
    }
}
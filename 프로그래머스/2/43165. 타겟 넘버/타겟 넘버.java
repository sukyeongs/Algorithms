class Solution {
    int answer = 0;
    public int solution(int[] numbers, int target) {
        dfs(numbers, target, 0, 0);
        return answer;
    }
    
    void dfs(int[] numbers, int target, int cur, int depth) {
        // depth == numbers.length 인데 target과 현재 값이 같다면 answer 증가
        // depth가 numbers.length보다 작으면 재귀 호출
        if(depth == numbers.length) {
            if(cur == target) answer++;
        } else {
            dfs(numbers, target, cur + numbers[depth], depth + 1);
            dfs(numbers, target, cur - numbers[depth], depth + 1);
        }
    }
}
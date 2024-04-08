import java.util.*;

class Solution {
    static Set<Integer> canMake;
    static boolean[] visited = new boolean[7];
    
    static int solution(String numbers) {
        int answer = 0;
        canMake = new HashSet<>();
        
        dfs(numbers, "", 0);
        
        // set의 숫자들 중 소수인 것 판별 + answer 값 증가
        for (Integer num: canMake) {
            if (isPrime(num)) answer++;
        }
        
        return answer;
    }
    
    // 숫자 만들고 set에 추가
    static void dfs(String numbers, String s, int depth) {
        if (depth > numbers.length()) return;
        
        for (int i = 0; i < numbers.length(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                canMake.add(Integer.parseInt(s + numbers.charAt(i)));
                dfs(numbers, s + numbers.charAt(i), depth+1);
                visited[i] = false;
            }
        }
    }
    
    static boolean isPrime(Integer num) {
        if (num < 2) return false;
        
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        
        return true;
    }

}
import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        int n = people.length;
        int answer = 0;
        int index = 0;
    
        Arrays.sort(people);
        for (int i = n - 1; i >= index; i--) {
            if (people[i] + people[index] <= limit) {
                answer++;
                index++;
            } else {
                answer++;
            }
        }
        
        return answer;
    }
}
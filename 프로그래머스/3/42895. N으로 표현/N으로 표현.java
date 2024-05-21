import java.util.*;

class Solution {
    public int solution(int N, int number) {
        int answer = -1;
        
        ArrayList<Set<Integer>> canMake = new ArrayList<>();
        for(int i = 0; i <= 8; i++) {
            canMake.add(new HashSet<>());
        }
        
        for(int i = 1; i <= 8; i++) {
            HashSet<Integer> eachCase = new HashSet<>();
            eachCase.add(Integer.parseInt(Integer.toString(N).repeat(i)));
            for(int j = 1; j < i; j++) {
                for(Integer num1 : canMake.get(j)) {
                    for(Integer num2 : canMake.get(i-j)) {
                        eachCase.add(num1 + num2);
                        eachCase.add(num1 - num2);
                        eachCase.add(num1 * num2);
                        if(num2 != 0) eachCase.add(num1 / num2);
                    }
                }
            }

            if(eachCase.contains(number)) {
                answer = i;
                break;
            }
            
            canMake.set(i, eachCase);
        }
        
        return answer;
    }
}
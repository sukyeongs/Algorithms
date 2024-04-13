import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int n = nums.length;
        HashSet<Integer> types = new HashSet<>();
        
        for(int num: nums) {
            types.add(num);
        }
        
        return Math.min(n/2, types.size());
    }
}
import java.util.*;

public class Solution {
    public static int[] solution(int[] answers) {
        int[] score = {0, 0, 0};
        int[] way1 = {1, 2, 3, 4, 5};
        int[] way2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] way3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        for(int i=0;i<answers.length; i++) {
            System.out.println(i);
            if(answers[i] == way1[i%5]) score[0]++;
            if(answers[i] == way2[i%8]) score[1]++;
            if(answers[i] == way3[i%10]) score[2]++;
        }
        
        int maxScore = Math.max(score[0], Math.max(score[1], score[2]));
        ArrayList<Integer> result = new ArrayList<>();
        if(score[0] == maxScore) result.add(1);
        if(score[1] == maxScore) result.add(2);
        if(score[2] == maxScore) result.add(3);
        
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}
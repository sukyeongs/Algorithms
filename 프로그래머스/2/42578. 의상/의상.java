import java.util.HashMap;
import java.util.ArrayList;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, ArrayList<String>> hasClothes = new HashMap<>();
        
        for (String[] c : clothes) {
            ArrayList<String> list = hasClothes.getOrDefault(c[1], new ArrayList<>());
            list.add(c[0]);
            hasClothes.put(c[1], list);
        }
        
        if(hasClothes.size() == 1) {
            for(String key : hasClothes.keySet()) {
                return hasClothes.get(key).size();
            }
        }
        
        for(String key: hasClothes.keySet()) {
            answer *= hasClothes.get(key).size() + 1;
        }
        
        return answer - 1;
    }
}
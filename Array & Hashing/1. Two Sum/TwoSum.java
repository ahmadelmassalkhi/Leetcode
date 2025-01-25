import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer j = map.get(nums[i]);
            if(j!=null) return new int[] {j, i};
            map.put(target-nums[i], i);
        }
        return null;
    }
}
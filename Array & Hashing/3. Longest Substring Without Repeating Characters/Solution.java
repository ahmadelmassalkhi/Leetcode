import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();

        int longest = 0;
        int start = 0;
        for (int i = 0; i < s.length(); i++) {
            if(map.containsKey(s.charAt(i)) && map.get(s.charAt(i)) >= start) {
                // set new start (directly after repeated character)
                start = map.get(s.charAt(i))+1;
            } else {
                // get max length
                longest = (i-start+1 > longest) ? i-start+1 : longest;
            }
            
            // cache
            map.put(s.charAt(i), i);
        }

        return longest;
    }
}
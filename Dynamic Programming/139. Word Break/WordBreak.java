import java.util.HashMap;
import java.util.List;


class Solution {
    HashMap<String, Boolean> map;

    private boolean helper(String s, List<String> wordDict) {
        if(s.isEmpty()) return true;
        if(map.containsKey(s)) return map.get(s);
        for (String word : wordDict) {
            if(s.startsWith(word)) {
                if(helper(s.substring(word.length()), wordDict)) return true;
            }
        }
        map.put(s, false);
        return false;
    }

    public boolean wordBreak(String s, List<String> wordDict) {
        map = new HashMap<>();
        return helper(s, wordDict);
    }
}
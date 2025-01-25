package Array.ValidAnagram;

class Solution {
    public boolean isAnagram(String s, String t) {
        // check for same length
        if(s.length() != t.length()) return false;

        // compute
        int[] charCount = new int[26];
        for (int i = 0; i < s.length(); i++) {
            charCount[s.charAt(i)-'a']++;
            charCount[t.charAt(i)-'a']--;
        } // incase of isAnagram, all should balance to 0

        // check for imbalances
        for (int count : charCount) {
            if(count < 0) return false;
        }

        return true;       
    }

}

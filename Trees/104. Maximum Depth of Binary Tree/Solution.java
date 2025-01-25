// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    public int maxDepth(TreeNode root) {
        if(root==null) return 0;
        int left = this.maxDepth(root.left);
        int right = this.maxDepth(root.right);
        return (left > right) ? left+1 : right+1; // +1 for the root
    }
}
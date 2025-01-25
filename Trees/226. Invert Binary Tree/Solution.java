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
    public TreeNode invertTree(TreeNode root) {
        // empty or leaf node
        if(root==null || (root.left==null && root.right==null)) return root;

        // invert left & right
        this.invertTree(root.left);
        this.invertTree(root.right);

        // invert root
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        return root;
    }
}
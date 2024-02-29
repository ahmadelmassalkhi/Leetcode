#include <stdio.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

/*************************************************************/

int helper(struct TreeNode* root, int *depth) {
    if(!root->left && !root->right) return root->val; // leaf node

    (*depth) += 1; // has at least one child => depth++
    if(!root->left) return helper(root->right, depth);
    if(!root->right) return helper(root->left, depth);

    int depthLeft = *depth;
    int depthRight = *depth;
    
    int left = helper(root->left, &depthLeft);
    int right = helper(root->right, &depthRight);

    // assign to max
    *depth = (depthLeft > depthRight) ? depthLeft : depthRight ;
    
    // choose max (prefer left if equal)
    if(depthLeft >= depthRight) return left;
    return right;
}

int findBottomLeftValue(struct TreeNode* root) {
    int depth = 0;
    return helper(root, &depth);
}

/*************************************************************/
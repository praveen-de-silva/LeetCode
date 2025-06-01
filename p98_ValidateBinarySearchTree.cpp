class Solution {
public:
    bool isValidBST(TreeNode* root) {
        // Base condition
        if (root==nullptr) {
            return true;
        }
        // cout << root->val << " ";

        if (root->left != nullptr) {
            // check with the highest left node
            TreeNode* crnt_L = root->left;
            while (crnt_L->right!=nullptr) {
                crnt_L = crnt_L->right;
            }
            if (crnt_L->val >= root->val) return false;
        }

        if (root->right != nullptr) {
            // check with the lowest right node
            TreeNode* crnt_R = root->right;
            while (crnt_R->left!=nullptr) {
                crnt_R = crnt_R->left;
            }
            if (crnt_R->val <= root->val) return false;
        }

        return isValidBST(root->left) && isValidBST(root->right);
    }
};
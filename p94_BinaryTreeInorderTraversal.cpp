#include <vector>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void inOrder(vector<int>& IOT, TreeNode* root) {
        if (root != nullptr) {
            inOrder(IOT, root->left);
            IOT.push_back(root->val);
            inOrder(IOT, root->right);
        }
    }

    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        inOrder(result, root);
        return result;
    }
};
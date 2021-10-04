// C++ program to find height of tree
#include <bits/stdc++.h>
using namespace std;
 
 
/* A binary tree node has data, pointer to left child
and a pointer to right child */
class node
{
    public:
    int data;
    node* left;
    node* right;
};
 
/* Compute the "maxDepth" of a tree -- the number of
    nodes along the longest path from the root node
    down to the farthest leaf node.*/
int height(node* root)
{
    if (root == NULL)
        return 0;
    else
    {
        /* compute the depth of each subtree */    
        /* use the larger one */
        return max(height(root->left),height(root->right))+1;
    }
}
 
/* Helper function that allocates a new node with the
given data and NULL left and right pointers. */
node* newNode(int data)
{
    node* root = new node();
    root->data = data;
    root->left = NULL;
    root->right = NULL;
     
    return(root);
}
     
// Driver code   
int main()
{
    node *root = newNode(1);
 
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
     
    cout << "Height of tree is " << height(root);
    return 0;
}
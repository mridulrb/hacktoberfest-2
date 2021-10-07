#include <bits/stdc++.h>
using namespace std;

struct Node{

    int data;
    Node *Left;
    Node *Right;

};

Node* CreateTree(int po[],int io[],int n){


    Node* node = (Node*)malloc(sizeof(Node));
    node->data = po[n-1];
    for(int i=0;i<n;i++){
        if (io[i] == po[n-1]){
            int nl = i;
            int nr = n-1-i;
            if(nl==0){
                node->Left = NULL;
            }
            else{
                int lio[nl];
                int lpo[nl];
                for(int j =0;j<i;j++){
                    lio[j] = io[j];
                    lpo[j] = po[j];
                }
                node->Left = CreateTree(lpo,lio,nl);
            }
            if(nr==0){
                node->Right = NULL;
            }
            else{
                int rio[nr];
                int rpo[nr];
                int ind=0;

                for(int j =i+1;j<n;j++){
                    rio[ind] = io[j];
                    ind++;
                }
                ind =0;
                for(int j =i;j<n-1;j++){
                    rpo[ind] = po[j];
                    ind++;
                }

                node->Right = CreateTree(rpo,rio,nr);
            }


        }
    }


    return (node);

}


void NonRecIo(Node * node){
stack<Node*> nodes;
Node *cur = node;
while(cur!=NULL || nodes.empty() == 0){

    if(cur != NULL){
        nodes.push(cur);
        cur = cur->Left;
    }
    else{
        cout<<nodes.top()->data<<" ";
        cur = nodes.top()->Right;
        nodes.pop();
    }
}

}

void LevelOrder(Node *node){

    queue<Node*> nodes;
    nodes.push(node);
    while(nodes.empty() == 0){
        Node *cur = nodes.front();
        if (cur->Left!=NULL)
            nodes.push(cur->Left);
        if(cur->Right != NULL)
            nodes.push(cur->Right);
        cout<<cur->data<<" ";
        nodes.pop();
    }

}

int main(){

    int n;

    cout<<"Enter Total number of elements of Tree--";
    cin>>n;
    int po[n];
    int io[n];
    cout<<"\nEnter PostOrder Traversal--\n";
    for(int i=0;i<n;i++){
        cin>>po[i];
    }
    cout<<"\nEnter InOrder Traversal--\n";
    for(int i=0;i<n;i++){
        cin>>io[i];
    }

    Node *root = CreateTree(po,io,n);

    cout<<"\nNon Recursive InOrder--\n";
    NonRecIo(root);

    cout<<"\nLevel Order Traversal--\n";
    LevelOrder(root);



return 0;
}

/*
Bubble Sort program in c++
Author: Shourya Gupta
*/
#include <iostream>
using namespace std;
int BubbleSort(int arr[],int n){
    int flag=0;
    for(int i=0; i<n-1; i++){
        int t=0;
        if(arr[i]>arr[i+1]){
            t=arr[i];
            arr[i]=arr[i+1];
            arr[i+1]=t;
            flag=1;
        }
    }
    if(flag==1){
        BubbleSort(arr, n);
    }
    else
        for(int i=0; i<n; i++){
            cout<<arr[i]<<" ";
        }
}
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }
    BubbleSort(arr,n);
}

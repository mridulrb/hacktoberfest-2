#include<iostream>
using namespace std;
   int n;
void insertionsort(int arr[],int n);
int main()
{

    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    insertionsort(arr,n);
    for(int i=0;i<n;i++)
    {
        cout<<arr[i];
    }

}
void insertionsort(int arr[],int n)//3 2 7 6 5 4 1
{
    int j,k;
    for(int i=1;i<n;i++)
    {
        int temp=arr[i];
        k=i;
        for(j=i-1;j>=0;j--)
        {
            if(arr[j]>arr[k])
                {arr[j+1]=arr[j];
                arr[j]=temp;
                k--;}

        }
        arr[j]=temp;
    }
}

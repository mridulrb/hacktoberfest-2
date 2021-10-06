#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
  int arr[1000],N;

  cout << "Enter the Size of Array : ";
  cin >> N;

  for(int i=0; i<N; i++)
  {
    cin >> arr[i];
  }

  cout << "Original arrray is : ";
  for(int i=0; i<N; i++)
  {
    cout << arr[i] << " " ;
  }
  
  reverse(arr,arr+N);

  cout << "\nReversed arrray is : ";
  for(int i=0; i<N; i++)
  {
    cout << arr[i] << " ";
  }
  cout << endl;
  return 0;

}

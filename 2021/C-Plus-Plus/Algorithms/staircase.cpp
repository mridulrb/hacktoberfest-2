#include<iostream>
using namespace std;

int main() 
{

  int height;
  cin>>height;

  int stair = height - 1;
    
  for (int i = 0; i < height; ++i)
  {
    for (int j = 0; j < height; ++j)
    {
      if (j >= stair)
        cout<<"#";
      else
        cout<<" ";
            
    }
      stair -= 1;
      cout<<endl;
  }    
    
  return 0;
}

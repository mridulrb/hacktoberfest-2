#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cin>>n;
	//print stair case;
	for(int i=1;i<=n;i++)
	{//outer loop
		for(int j=1;j<=n;j++)
		{
			//inner loop
			if(j>n-i)
			{
				cout<<"#";
			}
			else
			{
				cout<<" ";
			}
		}
		cout<<"\n";

	}
}
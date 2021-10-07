/*
    WAP which will take a single integer N as input. And will print starting N numbers from Fibonacci Series separated by space. And in the next line will print the sum of all the numbers which got printed on screen.
Input:

The first line contains a Single integer N as input 
Output:

In first line it will print N numbers from fibonacci series starting from 0

Second line will print the sum of all the numbers which we printed on screen
Sample Test Case 1

Input:

5

Output:

0 1 1 2 3
7

*/

#include<iostream>
using namespace std;

int main()
{
    int N,sum=0,num1=0,num2=1,res=1;

    cin >> N;
    cout << num1 << " " << num2 << " "; // Printing 1st two number of series.

    for(int i=0; i<N-2; i++)
    {
        sum = num1 + num2;

        // swapping values.
        num1 = num2;
        num2 = sum;
        
        cout << sum << " ";
        res = res+sum;
    }
    
    cout << endl << res << endl;
    return 0;
}
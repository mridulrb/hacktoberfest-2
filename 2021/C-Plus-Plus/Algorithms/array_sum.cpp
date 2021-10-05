// Function to find the sum of array integers

#include <iostream>
using namespace std;

int main()
{
    // taking input of the number of elements in the array
    int n;
    cin >> n;
    int array[n];
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> array[i]; //taking input of the elements of the array
        sum += array[i]; // adding the elements of the array to the variable sum
    }
    cout << sum << endl;
}
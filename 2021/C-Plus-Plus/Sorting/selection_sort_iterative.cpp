#include <algorithm>  ///for std::is_sorted
#include <array>      ///for std::array
#include <cassert>    ///for assert
#include <iostream>   ///for io operations

#include <iostream>
using namespace std;

namespace sorting {

int main() {
    int Array[6];
    cout << "\nEnter any 6 Numbers for Unsorted Array : ";

    // Input
    for (int i = 0; i < 6; i++) {
        cin >> Array[i];
    }


    // Selection Sorting
    for (int i = 0; i < 6; i++) {
        int min = i;
        for (int j = i + 1; j < 6; j++) {
            if (Array[j] < Array[min]) {
                min = j;  // Finding the smallest number in Array
void selectionSort(
    std::array<int, 8>& arr,
    int len) {  // Array size is const, can be modified by replacing "8" at (Ln
                // 45, Col 21) & (Ln 45, Col 60).
    for (auto it = 0; it < len; ++it) {
        int min = it;  // set min value
        for (auto it2 = it + 1; it2 < len + 1; ++it2) {
            if (arr[it2] < arr[min]) {  // check which element is smaller
                min = it2;  // store index of smallest element to min
            }
        }
        int temp = Array[i];
        Array[i] = Array[min];
        Array[min] = temp;
    }

    // Output
    cout << "\nSorted Array : ";
    for (int i = 0; i < 6; i++) {
        cout << Array[i] << "\t";
        if (min != it) {  // swap if min does not match to i
            int tmp = arr[min];
            arr[min] = arr[it];
            arr[it] = tmp;
        }
    }
}
}  // namespace sorting

static void test() {
    // testcase #1
    // [1, 0, 0, 1, 1, 0, 2, 1] return [0, 0, 0, 1, 1, 1, 1, 2]
    std::array<int, 8> array1 = {
        {1, 0, 0, 1, 1, 0, 2, 1}};  // Array size is const, can be modified by
                                    // replacing "8" at (Ln 71, Col 21).
    int array1size = array1.size();
    std::cout << "1st test... ";
    sorting::selectionSort(array1, array1size);
    assert(std::is_sorted(array1.begin(), array1.end()));
    std::cout << "Passed" << std::endl;

    // testcase #2
    // [19, 22, 540, 241, 156, 140, 12, 1] return [1, 12, 19, 22, 140, 156, 241,
    // 540]
    std::array<int, 8> array2 = {{19, 22, 540, 241, 156, 140, 12,
                                  1}};  // Array size is const, can be modified
                                        // by replacing "8" at (Ln 81, Col 21).
    int array2size = array2.size();
    std::cout << "2nd test... ";
    sorting::selectionSort(array2, array2size);
    assert(std::is_sorted(array2.begin(), array2.end()));
    std::cout << "Passed" << std::endl;

    // testcase #3
    // [11, 20, 30, 41, 15, 60, 82, 15] return [11, 15, 15, 20, 30, 41, 60, 82]
    std::array<int, 8> array3 = {{11, 20, 30, 41, 15, 60, 82,
                                  15}};  // Array size is const, can be modified
                                         // by replacing "8" at (Ln 90, Col 21).
    int array3size = array3.size();
    std::cout << "3rd test... ";
    sorting::selectionSort(array3, array3size);
    assert(std::is_sorted(array3.begin(), array3.end()));
    std::cout << "Passed" << std::endl;

    // testcase #4
    // [1, 9, 11, 546, 26, 65, 212, 14] return [1, 9, 11, 14, 26, 65, 212, 546]
    std::array<int, 8> array4 = {{1, 9, 11, 546, 26, 65, 212,
                                  14}};  // Array size is const, can be modified
                                         // by replacing "8" at (Ln 99, Col 21).
    int array4size = array2.size();
    std::cout << "4th test... ";
    sorting::selectionSort(array4, array4size);
    assert(std::is_sorted(array4.begin(), array4.end()));
    std::cout << "Passed" << std::endl;
}

int main() {
    test();  // run self-test implementations
    return 0;
} 

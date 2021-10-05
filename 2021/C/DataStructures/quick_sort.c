#include <stdio.h>


int main(){
    int x[6] = {4,2,6,3,1,5};
    quicksort(x,0,6);
    int i;
    printf("Sorted list according to the priority:\n");
    for (i = 0; i < 6; i++)
    {
        printf("%d  ",x[i]);
    }
    

    return 0;
}

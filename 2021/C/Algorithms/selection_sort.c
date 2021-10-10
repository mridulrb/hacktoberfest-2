// Selection sort
#include <stdio.h>
void swap(int *a, int *b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}
void selectionSort(int array[], int size)
{
	int step;
  for (step = 0; step < size - 1; step++)
  {
    int min_idx = step;
    int i;
    for (i = step + 1; i < size; i++)
    {
      if (array[i] < array[min_idx])
        min_idx = i;
    }
    swap(&array[min_idx], &array[step]);
  }
}
void printArray(int array[], int size)
{
	int i;
  for (i = 0; i < size; ++i)
  {
    printf("%d  ", array[i]);
  }
  printf("\n");
}
int main()
{
  int data[] = {20,16,18,15,17,19};
  int size = sizeof(data) / sizeof(data[0]);
  selectionSort(data, size);
  printf("Sorted Array:\n");
  printArray(data, size);
}

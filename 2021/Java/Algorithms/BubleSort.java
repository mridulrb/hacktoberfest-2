public class BubleSort {
    
    //method to short integer array using bublesort algortihm
    static void bubleSort(int[] array){
        for(int i = 0 ; i < array.length ; i++){
            for(int j = 0 ; j < array.length-1 ;j++){
                if (array[j+1] < array[j]){
                    int temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
    }

    //example
    public static void main(String[] args) {
        int [] array = {1,5,8,9,4,3};
        for(int i : array){
            System.out.print(i + ",");
        }
        bubleSort(array);
        System.out.println("");
        for(int i : array){
            System.out.print(i + ",");
        }
    }
}

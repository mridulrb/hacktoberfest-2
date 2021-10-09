/*
Sample Input1-:
3
99
99
99

Output:
9
*/

interface SumInterface{
    int compute(int n);
}
public class CalSum implements SumInterface{
    public int compute(int n){
        int sum=0;
        while(n>0 || sum>9){
            if(n==0){
                n=sum;
                sum=0;
            }
            sum+=n%10;
            n/=10;
        }
        return sum;
    }
    int elementsArraySum(int arr[]){
        int sum=0;
        for(int i:arr)
            sum+=i;
        return sum;
    }
}

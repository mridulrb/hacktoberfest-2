
import java.util.Scanner;

class fibonacci_numbers {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        int n=in.nextInt();
        int a=0;
        int b=1;
        int c=1;
        while (a<=n){
            System.out.println(a);
            a=b;
            b=c;
            c=a+b;
        }

    }
}
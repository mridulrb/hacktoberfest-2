/**
  * Generates a license plate number
*/

public class Ex4_25 {
  public static void main(String[] args) {
    
    //initialize digits and letter variables
    int num1, num2, num3, num4;
    char letter1, letter2, letter3;
    
    //randomly generate numbers between 0 and 10
    num1 = (int)(Math.random() * 10);
    num2 = (int)(Math.random() * 10);
    num3 = (int)(Math.random() * 10);
    num4 = (int)(Math.random() * 10);
    
    //randomly generate capital letters (65-90 ASCII)
    //cast to char    
    letter1 = (char)((int)(Math.random() * 26 + 65));
    letter2 = (char)((int)(Math.random() * 26 + 65));
    letter3 = (char)((int)(Math.random() * 26 + 65));
    
    System.out.println("The plate number is: " + letter1 + letter2 + letter3 + num1 + num2 + num3 + num4);
    
  }
}

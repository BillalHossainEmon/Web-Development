package ReturningVal;
import java.util.Scanner;

public class TestRun {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		ReturningValue ob1 = new ReturningValue();
		System.out.print("Enter a value: ");
		int val = input.nextInt();
		
		int result = ob1.square(val);
		System.out.print("The square of the value is: "+result);
		
	}
		

}

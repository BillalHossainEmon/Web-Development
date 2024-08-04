package ArithmeticExercise;
import java.util.Scanner;

public class Conditional {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int num;
		
		System.out.print("Enter a number: ");
		num = input.nextInt();
		
		if(num>0) {
			System.out.print("The number is positive");
		}
	}
}

package Arithmetic;
import java.util.Scanner;

public class Extercise {
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		int num;
		
		System.out.print("Enter your number: ");
		num = input.nextInt();
		
		if(num<0) {
			System.out.print("The number is negative");
		}
		
		else {
			System.out.print("The number is positive");
		}
		
	}
	

}

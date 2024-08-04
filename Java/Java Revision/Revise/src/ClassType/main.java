package ClassType;
import java.util.Scanner;

public class main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		Teacher t1 = new Teacher();
		t1.name = "Emon";
		t1.age = 24;
		t1.qualification = "BSc in CSE";
		t1.displayInformation2();
		
		Teacher t2 = new Teacher();
		System.out.println("Enter your name: ");
		t2.name = input.nextLine();
		System.out.println("Enter your qualification: ");
		t2.qualification = input.nextLine();
		System.out.println("Enter your age: ");
		t2.age = input.nextInt();
		t2.displayInformation2();
	}

}

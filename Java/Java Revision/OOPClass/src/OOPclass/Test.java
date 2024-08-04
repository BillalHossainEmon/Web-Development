package OOPclass;
import java.util.Scanner;

public class Test {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		Teacher Teacher1 = new Teacher("Emon", "Uttara", 1626201933);
		Teacher1.displayInformation();
		
		Teacher Teacher2 = new Teacher("Shupti", "Banasree", 162);
		Teacher2.displayInformation();
	}
}

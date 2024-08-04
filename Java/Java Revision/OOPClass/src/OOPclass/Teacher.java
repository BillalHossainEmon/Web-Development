package OOPclass;

public class Teacher {
	String name;
	String Address;
	int Phone;
	
	Teacher(String n, String a, int p){
		name = n;
		Address = a;
		Phone = p;
	}
	
	void displayInformation() {
		System.out.println("Name : "+name);
		System.out.println("Address : "+Address);
		System.out.println("Phone : "+Phone);
		System.out.print("\n\n");
	}
}

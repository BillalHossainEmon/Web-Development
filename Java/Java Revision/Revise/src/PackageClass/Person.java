package PackageClass;

public class Person {
	String name;
	String address;
	double phone;
	
	Person(String n, String a, double p){
		name = n;
		address = a;
		phone = p;
	}
	
	void displayInformation() {
		System.out.println("Name: "+name);
		System.out.println("Address: "+address);
		System.out.println("Phone: "+phone);
		System.out.println("\n\n");
	}

}

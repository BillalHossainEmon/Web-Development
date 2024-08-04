package GetterSetter;

public class main {
	public static void main(String[] args) {
		person p1 = new person();
		p1.setName("Emon");
		System.out.println(p1.getName());
		p1.setAge(24);
		System.out.println(p1.getAge());
	}
}

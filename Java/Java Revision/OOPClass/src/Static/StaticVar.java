package Static;

public class StaticVar {
	static int count = 0;
	
	StaticVar(){
		count++;
	}
	
	void total() {
		System.out.println(+count);
	}

}

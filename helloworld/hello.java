public class Hello(){
	String myName;
	
	public Hello(){
		myName="Duke";
	}
	
	public void sayHello(){
		System.out.println("Hello" + myName);
	}
}

publica class Client{
	public static void main(String[] args){
		Hello h = new Hello();
		h.sayHello()
	}
}
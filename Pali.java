import java.util.Scanner;



public class Pali {
	
	public void palin() {
		
		Scanner oScan = new Scanner(System.in);
		System.out.println("Enter a word");
		String word = oScan.nextLine();
		String temp = "";
		char[] words = word.toCharArray();
		
		for (int i = words.length - 1; i >= 0; i--){
			
			temp += words[i];
			
		
		}
		if (word.equals(temp)) {
			System.out.println("Is a palindrome");
		 
		}
		else {
			System.out.println("Isn't a palindrome");
		}
	}

}

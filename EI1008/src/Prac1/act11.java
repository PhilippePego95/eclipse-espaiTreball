//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

public class act11 {

	public static void main(String[] args) {
		System.out.println(esSufijo("ab cd", "bbc lll"));
		System.out.println(esSufijo("la casa de papel", "papel"));
		System.out.println(esSufijo("el gato lopez", "to lopez"));
		System.out.println(esSufijo("el cotxe gro", " "));

	}

	public static boolean esSufijo(String a, String b) {
		if (b.length() >= a.length()) {
			return false;
		} else {
			for (int i = 1; i <= b.length(); i++) {
				if (a.charAt(a.length() - i) != b.charAt(b.length() - i)) {
					return false;
				}
			}

		}
		return true;
	}

}

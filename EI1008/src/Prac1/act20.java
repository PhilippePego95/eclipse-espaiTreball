//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

public class act20 {

	public static void main(String[] args) {
		
		test();
	}

	public static void test() {
		boolean si = true;

		int[] buid = {};
		int[] vector = { 6, 1, 2, 3, 5 };
		int[] vector1 = { 6, 2, 1 };
		int[] vector2 = { 7 };

		if (!contiene(vector, vector1)) {
			si = false;
		}
		if (!contiene(vector, buid)) {
			si = false;
		}
		if (contiene(vector2, vector1)) {
			si = false;
		}

		if (si) {
			System.out.println("Totes les proves passen el test");
		} else {
			System.out.println("No passa el test");
		}

	}

	public static boolean contiene(int[] vector, int n) {
		// for (int num : vector) {
		for (int i = 0; i < vector.length; i++) {
			if (vector[i] == n) {
				return true;
			}
		}
		return false;
	}

	public static boolean contiene(int[] vector, int[] vector2) {
		// for (int num : vector2) {
		for (int i = 0; i < vector2.length; i++) {
			if (!contiene(vector, vector2[i])) {
				return false;
			}
		}
		return true;

	}

}

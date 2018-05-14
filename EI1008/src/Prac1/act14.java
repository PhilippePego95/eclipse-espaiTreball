//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

public class act14 {
	public static void main(String[] args) {
		int[] vector = { 1, 2, 3, 4, 2, 4 };
		int[] vector1 = { };
		// System.out.println(últimaPosición(vector, 2));
		test(vector,vector1);
	}

		public static void test(int[] vector,int []vector1) {
		boolean si = true;
		if (últimaPosición(vector, 2) != 4) {
			si = false;
		}
		if (últimaPosición(vector, 1) != 0) {
			si = false;

		}
		if (últimaPosición(vector, 3) != 2) {
			si = false;
		}
		if (últimaPosición(vector, 7) > 0) {
			si = false;
		}
		if (últimaPosición(vector1, 7) >0) {
			si = false;
		}
		if(si) {
			System.out.println("Totes les proves passen el test");
		}else {
			System.out.println("No passa el test");
		}

	}

	public static int últimaPosición(int[] vector, int num) {
		int pos = -1;
		for (int i = 0; i < vector.length; i++) {
			if (vector[i] == num) {
				pos = i;
			}
		}
		return pos;

	}

}

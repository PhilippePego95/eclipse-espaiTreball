//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

public class act23 {

	public static void main(String[] args) {
		test();

	}
	public static void test() {
		boolean si = true;

		int[][] matriu = { { 1, 2, 3, 4, 5, 6 }, 
						   { 7, 1, 7, 2, 6, 7 }, 
						   { 5, 2, 1, 6, 2, 2 }, 
						   { 6, 3, 6, 1, 5, 1 },
						   { 2, 6, 2, 4, 1, 4 } };
		int[][]matriu2= {{0}};
		
		if (!estáEnTodasLasColumnas(matriu, 2)) {
			si = false;
		}
		if (!estáEnTodasLasColumnas(matriu, 1)) {
			si = false;
		}
		if (estáEnTodasLasColumnas(matriu, 8)) {
			si = false;
		}
		if (estáEnTodasLasColumnas(matriu2, 8)) {
			si = false;
		}
	
		if (si) {
			System.out.println("Totes les proves passen el test");
		} else {
			System.out.println("No passa el test");
		}
	}

	public static boolean estáEnTodasLasColumnas(int[][] matriu, int num) {
		boolean esta;
		for (int i = 0; i < matriu[0].length; i++) {
			esta = false;
			for (int j = 0; j < matriu.length; j++) {
				if (matriu[j][i] == num) {
					esta = true;
					break;

				}
			}
			if (esta == false) {
				return false;
			}
		}

		return true;
	}

}

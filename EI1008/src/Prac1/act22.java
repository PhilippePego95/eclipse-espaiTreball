//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

public class act22 {
	public static void main(String[] args) {
		double[][] matriu = { { 1, -2, -3, -4, 1, -8, -5 }, { -1, -2, 3, -4, -5, 1, 2, -5, -6 } };
		System.out.println(másOlasDeFrío(matriu, 8));
	}

	public static int másOlasDeFrío(double[][] matriu, int n) {
		int nMax = 0;
		int any = 0;
		for (int i = 0; i < matriu.length; i++) {
			int num = contarOlasDeFrío(matriu[i], n);

			if (num > nMax){
				nMax = num;
				any = i;
			}

		}
		if (nMax > 0) {

			return (any + 1900);
		} else {
			return -1;
		}

	}

	public static int contarOlasDeFrío(double[] vector, int n) {
		int cont = 0, ola = 0;
		for (int i = 0; i < vector.length; i++) {
			if (vector[i] < 0) {
				cont++;
			} else {
				if (cont > n) {
					ola++;
				}
				cont = 0;
			}
		}
		if (cont > n) {
			ola++;
		}
		return ola;
	}
}

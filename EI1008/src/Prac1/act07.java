//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

import java.util.Scanner;

public class act07 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Introduce un número entero: ");
		int num = scanner.nextInt();
		System.out.println(esPrimo(num));
		scanner.close();

	}

	public static boolean esPrimo(int n) {
		int cont = 0;
		for (int i = 2; i < n; i++) {
			if (n % i == 0) {
				cont++;
			}
		}
		if (cont == 0) {
			return true;

		} else {
			return false;
		}

	}

}

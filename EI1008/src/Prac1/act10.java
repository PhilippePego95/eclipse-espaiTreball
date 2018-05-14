//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

import java.util.Scanner;

public class act10 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Introduce un número entero: ");
		int num = scanner.nextInt();
		scanner.close();
		int maxDiv = 0, maxNum = 0, n;
		for (int i = 1; i <= num; i++) {

			n = contarDivisores(i);
			if (n >= maxDiv) {
				maxDiv = n;
				maxNum = i;
			}
		}
		System.out.println("El número con más divisores es " + maxNum + " (" + maxDiv + " divisores)");
	}

	public static int contarDivisores(int n) {
		int total = 0;
		for (int i = 1; i <= n; i++) {
			if (n % i == 0) {
				total++;
			}
		}

		return total;
	}

}

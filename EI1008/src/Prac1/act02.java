//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

import java.util.Scanner;

public class act02 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Introduce un número entero: ");
		int num = scanner.nextInt();
		scanner.close();
		long fact = 1;
		if (num == 0 || num == 1) {
			System.out.println(num + "!! =  1");

		} else {

			if (num % 2 == 0) {
				for (int i = 2; i <= num; i += 2) {
					fact *= i;

				}
				System.out.println(num + "!! = " + fact);

			} else {
				for (int i = 1; i <= num; i += 2) {
					fact *= i;

				}
				System.out.println(num + "!! = " + fact);

			}
		}
	}

}
//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

import java.util.Scanner;

public class act06 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Introduce un número entero: ");
		int num = scanner.nextInt();
		scanner.close();
		int nmas = 0, ndiv = 0, cont = 0;

		for (int i = 1; i <= num; i++) {
			cont = 0;
			for (int j = 1; j <= i; j++) {
				if (i % j == 0) {
					cont++;
				}
			}
			if (cont >= ndiv)

			{
				nmas = i;
				ndiv = cont;
			}
		}
		System.out.println("El número con más divisores es " + nmas + " (" + ndiv + " divisores)");
	}

}

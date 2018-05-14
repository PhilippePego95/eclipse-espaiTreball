//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

import java.util.Scanner;

public class act05 {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		System.out.print("Introduce un número entero: ");
		int num = scanner.nextInt();
		scanner.close();
		int cont = 0;
		long primo=1;
		for (int i = 1; i <=num; i++) {
			cont=0;
			for (int j = 1; j <= i; j++) {
				if (i % j == 0) {
					cont++;
				}
			}
			if (cont == 2) {
				primo*=i;
			} 
		}
		System.out.print(num+"# = "+primo);

	}

}

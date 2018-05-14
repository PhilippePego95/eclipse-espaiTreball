//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

import java.util.Scanner;

public class act04 {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		System.out.print("Introduce un número entero: ");
		int num = scanner.nextInt();
		scanner.close();
		System.out.print("Los números primos menores que "+num+" son: ");
		int cont = 0;
		for (int i = 1; i <num; i++) {
			cont=0;
			for (int j = 1; j <= i; j++) {
				if (i % j == 0) {
					cont++;
				}
			}
			if (cont == 2) {
				System.out.print(i+" ");
			} 
		}
	}

}

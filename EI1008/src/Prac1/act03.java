//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

import java.util.Scanner;

public class act03 {
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		System.out.print("Introduce un número entero: ");
		int num = scanner.nextInt();
		scanner.close();
		int cont=0;
		for (int i = 2; i < num; i++) {
			if(num%i==0) {
				cont++;			
				}
		}
		if (cont==0) {
			System.out.println("Es primo");
		}else {
			System.out.println("No es primo");
		}
	}

}
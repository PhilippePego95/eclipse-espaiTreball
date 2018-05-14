//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

import java.util.Scanner;

public class act01 {

	public static void main(String[] args) {
		Scanner scanner= new Scanner(System.in);
		System.out.print("Introduce un número entero: ");
		int num=scanner.nextInt();		
		scanner.close();
		long fact=1;
		for(int i=1;i<=num;i++) {
			fact*=i;
			
		}
		System.out.println(num+"! = "+fact);
	}

}

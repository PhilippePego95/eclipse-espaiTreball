package practica2.ejercicio05;

import java.util.Scanner;

public class aniversariv2 {

	public static void main(String[] args) {
		Scanner leer = new Scanner(System.in);
		Fecha aniversari = new Fecha(7, 5, 1995);
		boolean correcte = false;
		int contador = 0;
		Fecha máximaFechaAnterior = new Fecha(1, 1, 2010);
		Fecha mínimaFechaAnterior = new Fecha(1, 1, 1900);

		while (!correcte) {
			System.out.println("\nIntrodueix la data: ");

			// 1/1/2010 1/1/1990

			System.out.print("dia: ");
			int dia = leer.nextInt();

			System.out.print("mes :");
			int mes = leer.nextInt();

			System.out.print("any: ");
			int any = leer.nextInt();
			Fecha data = new Fecha(dia, mes, any);
			contador++;
			if (data.getAño() > 1900 && data.getAño() < 2010) {
				if (máximaFechaAnterior.compareTo(data) < 0) {
					System.out.println("Intento sin sentido");
				} else if (mínimaFechaAnterior.compareTo(data) > 0) {
					System.out.println("Intento sin sentido");

				} else {

					int res = data.compareTo(aniversari);
				//	System.out.println(res);
					if (res == 0) {
						System.out.println("Es la data d'aniversari");
						correcte = true;
					} else if (res > 0) {
						System.out.println("La data es gran");
						máximaFechaAnterior = data;
					} else {
						System.out.println("La data es menuda");
						mínimaFechaAnterior = data;
					}
				}
			} else {
				System.out.println("Data no acceptada");

			}

		}
		System.out.println("Intents: " + contador);
		leer.close();

	}
}

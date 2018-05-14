package practica2.ejercicio08;

import java.util.Scanner;

public class aniversariv2 {

	public static void main(String[] args) throws ExcepcionFechaInvalida {
		Scanner leer = new Scanner(System.in);
		Fecha aniversari = new Fecha(27, 4, 1989);
		boolean correcte = false;
		int contador = 0;
		Fecha máximaFechaAnterior = new Fecha(1, 1, 2010);
		Fecha mínimaFechaAnterior = new Fecha(1, 1, 1900);
		int dia = 0, mes = 0, any = 0;
		
		while (!correcte) {
			System.out.println("\nIntrodueix la data: ");
			Fecha data;
			// 1/1/2010 1/1/1990
			boolean hayError;
			do {
				hayError = false;
				try {
					System.out.print("dia: ");
					dia = leer.nextInt();

					System.out.print("mes :");
					mes = leer.nextInt();

					System.out.print("any: ");
					any = leer.nextInt();

					data = new Fecha(dia, mes, any);
				} catch (ExcepcionFechaInvalida e) {
					System.out.println("La data no es acceptada");
					contador++;
					hayError = true;

				}
			} while (hayError);

			data = new Fecha(dia, mes, any);

			contador++;
			if (data.getAño() > 1900 && data.getAño() < 2010) {
				if (máximaFechaAnterior.compareTo(data) < 0) {
					System.out.println("Intent sense sentit");
				} else if (mínimaFechaAnterior.compareTo(data) > 0) {
					System.out.println("Intent sense sentit");

				} else {

					int res = data.compareTo(aniversari);
					// System.out.println(res);
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

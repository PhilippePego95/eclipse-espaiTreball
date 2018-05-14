package practica2.ejercicio08;

import java.util.Scanner;

public class aniversari {
	public static void main(String[] args) throws ExcepcionFechaInvalida {
		Scanner leer = new Scanner(System.in);
		Fecha aniversari = new Fecha(7, 5, 1995);
		boolean correcte = false;
		int contador = 0;

		while (!correcte) {
			System.out.println("\nIntrodueix la data: ");
			int dia=0, mes=0, any=0;

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
					
					dataValida(dia, mes, any);
				} catch (ExcepcionFechaInvalida e) {
					System.out.println("La data no es acceptada");
					contador++;
					hayError = true;
				 
				}
			} while (hayError);

			Fecha data = new Fecha(dia, mes, any);
			contador++;
			if (data.getAño() > 1900 && data.getAño() < 2010) {
				int res = data.compareTo(aniversari);
				if (res == 0) {
					System.out.println("Es la data d'aniversari");
					correcte = true;
				} else if (res > 0) {
					System.out.println("La data es gran");
				} else {
					System.out.println("La data es menuda");
				}
			} else {
				System.out.println("Data no acceptada");

			}
		}
		System.out.println("Intents: " + contador);
		leer.close();

	}

	public static void dataValida(int dia, int mes, int any) throws ExcepcionFechaInvalida {
		if (mes > 12 || dia >= Fecha.díaMes(mes, any))
			throw new ExcepcionFechaInvalida();
		
	}
}

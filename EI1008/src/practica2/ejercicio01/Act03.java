package practica2.ejercicio01;

import java.io.FileNotFoundException;
import java.util.Scanner;

public class Act03 {

	public static void main(String[] args) throws FileNotFoundException {
		Scanner leer = new Scanner(System.in);
		System.out.println("Indique su posición actual");
		System.out.print("Coordenada X: ");
		int x = leer.nextInt();
		System.out.print("Coordenada Y: ");
		int y = leer.nextInt();
		Punto punt = new Punto(x, y);

		System.out.print("Introduce el nombre del fichero de texto: ");
		String fitxer = leer.next();
		leer.close();
		//	fitxer = "datos/restaurantes.txt";
		// Restaurante pub = new Restaurante("El Moss", punt, 7);

		Restaurante[] llista = Restaurante.leeRestaurantes(fitxer);
		Restaurante bar=restauranteMásPróximo(llista, punt);
		
		System.out.println("El restaurante más cercano a su posición es" + bar.getNombre() + ", situado en el punto "
				+ bar.getPosición());

	}

	public static Restaurante restauranteMásPróximo(Restaurante[] llista, Punto punt) {
		// for(int pos=0;pos<llista.length;pos++) {
		Restaurante maxim = llista[0];

		for (Restaurante bar : llista) {
			if (bar.distancia(punt) < maxim.distancia(punt)) {
				maxim = bar;
			}
		}
		return maxim;
	
	}

}

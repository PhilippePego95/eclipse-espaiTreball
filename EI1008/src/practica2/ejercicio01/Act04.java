package practica2.ejercicio01;

import java.io.FileNotFoundException;
import java.util.Scanner;

public class Act04 {

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
		fitxer = "datos/restaurantes.txt";

		Restaurante[] llista = Restaurante.leeRestaurantes(fitxer);
		Restaurante bar=restauranteMejorValorado(llista, punt,8);
		System.out.println(bar.toString());
		//System.out.println("El restaurante más cercano a su posición es" + bar.getNombre() + ", situado en el punto "
			//	+ bar.getPosición());
		
	}

	public static Restaurante restauranteMejorValorado(Restaurante[] llista, Punto punt,double distancia) {
		// for(int pos=0;pos<llista.length;pos++) {
		Restaurante maxim = llista[0];

		for (Restaurante bar : llista) {
			if (bar.distancia(punt) <= distancia && bar.getValoración()>maxim.getValoración()) {
				maxim=bar;
				
			}
		}
		return maxim;

	}

}

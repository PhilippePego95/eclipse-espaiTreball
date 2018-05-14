package practica2.ejercicio01;

import java.io.FileNotFoundException;
import java.util.Arrays;

public class Act02 {

	public static void main(String[] args) throws FileNotFoundException {
		Punto punt = new Punto(2, 2);
		Punto p = new Punto(4, 4);

		Restaurante pub = new Restaurante("El Moss", punt, 7);
		
		System.out.println(pub.getNombre());
		System.out.println(pub.getPosición());
		System.out.println(pub.getValoración());
		System.out.println(pub.distancia(p));

	  //System.out.println(Arrays.toString(pub.leeRestaurantes("datos/pubs.txt")));

		Restaurante[] llista = Restaurante.leeRestaurantes("datos/pubs.txt");
		llista = Restaurante.leeRestaurantes("datos/restaurantes.txt");

		System.out.println(Arrays.toString(llista));
	}

}


package practica2.ejercicio01;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Restaurante {
	private String nombre;
	private Punto posición;
	private int valoración;

	public Restaurante(String nombre, Punto posición, int valoración) {
		this.nombre = nombre;
		this.posición = posición;
		this.valoración = valoración;
	}

	public String getNombre() {
		return nombre;
	}

	public Punto getPosición() {
		return posición;
	}

	public int getValoración() {
		return valoración;
	}

	public double distancia(Punto p) {
		return posición.distancia(p);
	}

	public static Restaurante[] leeRestaurantes(String nombreFichero) throws FileNotFoundException {
		
		Scanner entrada = new Scanner(new File(nombreFichero));
		int tamany = entrada.nextInt();
		Restaurante llista[] = new Restaurante[tamany];
		int x, y, puntuació, n = 0;
		String nom;

		while (entrada.hasNextLine()) {
			
			x = entrada.nextInt();
			y = entrada.nextInt();
			puntuació = entrada.nextInt();
			nom = entrada.nextLine();
			
			Punto lloc = new Punto(x, y);			
			Restaurante pub = new Restaurante(nom, lloc, puntuació);
			
			llista[n] = pub;
			n++;
		}

		entrada.close();
		return llista;
	}
	public String toString() {
		return nombre+" "+ valoración+" "+posición;
	}

}

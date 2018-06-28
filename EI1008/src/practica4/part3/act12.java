package practica4.part3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class act12 {
	public static void main(String[] args) throws FileNotFoundException {
		String[] dnisCenso = crearVectorDni("datos/dniCensoOrdenado.txt");
		String[] dnisClientes = crearVectorDni("datos/dniClientesOrdenado.txt");
		long tiempoInicio = System.currentTimeMillis();
		int coincidencias = contarCoincidencias(dnisCenso, dnisClientes);
		long tiempoTranscurrido = System.currentTimeMillis() - tiempoInicio;

		System.out.println("He encontrado " + coincidencias + " coincidencias (empleando " + tiempoTranscurrido
				+ " milisegundos)");

	}

	public static String[] crearVectorDni(String fichero) throws FileNotFoundException {
		Scanner entrada = new Scanner(new File(fichero));
		int n = entrada.nextInt();
		String[] vector = new String[n];
		int pos = 0;
		while (entrada.hasNext()) {
			vector[pos++] = entrada.next();
		}
		entrada.close();

		return vector;
	}

	public static int contarCoincidencias(String[] v1, String[] v2) {
		int can = 0;
		int i = 0, j = 0;
		while (i < v1.length && j < v2.length) {
			
			int comp=v1[i].compareTo(v2[j]);
			if (comp > 0) {
				j++;
			} else if (comp < 0) {
				i++;
			} else if (comp==0) {
				can++;
				i++;
				j++;

			}
		}
		
		while (i < v1.length) {
			if (v1[i].equals(v2[j])) {
				can++;

			}
			i++;
		}
		while (j < v2.length) {
			if (v1[i-1].equals(v2[j])) {
				can++;

			}
			j++;
		}
		return can;
	}
}

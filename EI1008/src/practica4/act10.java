package practica4;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class act10 {

/*	public static void main(String[] args) throws FileNotFoundException {
		String fichero="dniClientes.txt";
		String [] v=crearVectorDni(fichero);
			
			
	}*/
	public static void main(String[] args) throws FileNotFoundException {
		String[] dnisCenso = crearVectorDni("datos/dniCenso.txt");
		String[] dnisClientes = crearVectorDni("datos/dniClientes.txt");

		long tiempoInicio = System.currentTimeMillis();
		int coincidencias = contarCoincidencias(dnisCenso, dnisClientes);
		long tiempoTranscurrido = System.currentTimeMillis() - tiempoInicio;

		System.out.println("He encontrado " + coincidencias
				+ " coincidencias (empleando " + tiempoTranscurrido
				+ " milisegundos)");

	}
	public static String[] crearVectorDni(String fichero) throws FileNotFoundException {
		Scanner entrada = new Scanner(new File(fichero));
		int n=entrada.nextInt();
		String[] vector=new String[n];
		int pos=0;
		while (entrada.hasNext()) {
			vector[pos++]=entrada.next();
		}	
		entrada.close();
		
		return vector;
	}
	public static boolean buscarDni(String dni,String[] v) {
		for(String dato:v) {
			if(dni.equals(dato)) {
				return true;
			}
		}
		return false;		
	}
	public static int contarCoincidencias(String[] v1,String[] v2) {
		int can=0;
		for(String dni:v1)
				if(buscarDni(dni,v2))
					can++;
		return can;
	}

}

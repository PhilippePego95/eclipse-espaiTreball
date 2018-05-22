package practica3.ejercicio04;

import java.io.File;
import java.io.FileNotFoundException;

import java.util.Scanner;

public class PalabraMasFrecuente {

	public static void main(String[] args) throws FileNotFoundException {
	
		long inici=System.currentTimeMillis();
	    String llibre="DonQuijote.txt";
		
		
		//String llibre="AlicesAdventuresInWonderland.txt";
		Diccionario dic=new Diccionario();
		Scanner entrada = new Scanner(new File("datos/"+llibre));

		while (entrada.hasNext()) {
			String palabra=entrada.next();
			dic.añadir(palabra, 1);
		}
		entrada.close();
		String palabra=dic.cadenaConMayorCantidad();
		System.out.println("La palabra más frecuente en "+llibre+" es <<"+palabra+">> con "+dic.cantidad(palabra)+" aparaciones.");

		long fin=System.currentTimeMillis();

	    System.out.println("temps d'ejecució: "+((fin-inici)/1000.0)+" segundos");
	
	}


}

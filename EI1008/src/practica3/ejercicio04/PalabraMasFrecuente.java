package practica3.ejercicio04;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Calendar;
import java.util.Scanner;

public class PalabraMasFrecuente {

	public static void main(String[] args) throws FileNotFoundException {
		int hora, minutos, segundos;
		Calendar calendario = Calendar.getInstance();
		hora =calendario.get(Calendar.HOUR_OF_DAY);
	    minutos = calendario.get(Calendar.MINUTE);
	    segundos = calendario.get(Calendar.SECOND);
	    System.out.println(hora + ":" + minutos + ":" + segundos);
		
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
		Calendar calendari = Calendar.getInstance();

		int hora1 =calendari.get(Calendar.HOUR_OF_DAY);
	    int minutos1 = calendari.get(Calendar.MINUTE);
	    int segundos1 = calendari.get(Calendar.SECOND);
	    System.out.println(hora1 + ":" + minutos1 + ":" + segundos1);
	    int segons= ((minutos1*60)+segundos1)-((minutos*60)+segundos);
	   
	    System.out.println("temps d'ejecució: "+((double)segons/60)+" minuts");
	
	}


}

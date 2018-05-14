package practica3.ejercicio04;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class GanadorLiga {
	public static void main(String[] args) throws FileNotFoundException {
		String llibre="liga2015-2016.txt";
	  	Diccionario dic=new Diccionario();
		Scanner entrada = new Scanner(new File("datos/"+llibre));

		while (entrada.hasNext()) {
			
			String local = entrada.next();
			int golLoc = entrada.nextInt();
			String visitante = entrada.next();
			int golVis = entrada.nextInt();
			
			if(golLoc >golVis ){
				dic.añadir(local,3);
				
			}else if (golLoc < golVis ){
				dic.añadir(visitante,3);
			}else {
				dic.añadir(local,1);
				dic.añadir(visitante,1);

			}
		}
		entrada.close();
		String equip=dic.cadenaConMayorCantidad();
		System.out.println("Ganador de liga 2015-2016: <<"+equip+">> con "+dic.cantidad(equip)+" puntos.");

	}

}

//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class act24 {

	public static void main(String[] args) throws FileNotFoundException {
		String[] vector = { "Athletic_Club", "SC_Huelva", "SD_Lagunak" };
		
		char[][] matriu = crearMatrizResultado(vector, "datos/liga.txt");
		for (int i = 0; i < matriu.length; i++)
			System.out.println(Arrays.toString(matriu[i]));

	}

	public static int indice(String[] vector, String equipo) {
		int pos = 0;
		for (int i = 0; i < vector.length; i++) {
			if (vector[i].equals(equipo)) {
				pos = i;
			}
		}
		return pos;
	}

	public static char[][] crearMatrizResultado(String[] vector, String fitxer) throws FileNotFoundException {

		char matriu[][] = new char[vector.length][vector.length];
		Scanner entrada = new Scanner(new File(fitxer));
		String local, visitante;
		int golesLocal, golesVisitantes;
	
		
		for (int i = 0; i < vector.length; i++) {
			for (int j = 0; j < vector.length; j++) {
				matriu[i][j] = '-';
			}
		}
		
		
		int posLoc, posVis;
		while (entrada.hasNextLine()) {
			local = entrada.next();
			golesLocal = entrada.nextInt();
			visitante = entrada.next();
			golesVisitantes = entrada.nextInt();
			posLoc = indice(vector, local);
			posVis = indice(vector, visitante);

			if (golesLocal > golesVisitantes) {
				matriu[posLoc][posVis] = '1';
			} else if (golesLocal < golesVisitantes) {
				matriu[posLoc][posVis] = '2';
			} else {
				matriu[posLoc][posVis] = 'X';

			}

		}
		entrada.close();
		return matriu;

	}
}

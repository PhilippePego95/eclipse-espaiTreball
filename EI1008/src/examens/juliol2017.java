package examens;

import java.util.Arrays;

public class juliol2017 {
	public static void main(String[] args) {
		String [] vec=new String[0];
	//	double nota=0;
		System.out.println(Arrays.toString(vec));

		String[] llista = { "ana", "berta", "phil", "phil", "x" };
		System.out.println(Arrays.toString(llista));
		llista = añadir(llista, "berta");
		System.out.println(Arrays.toString(llista));
		String mas = masRepetido(llista);
		String[] vector = { "a", "ana", "laia", "isa", "phil", "x" };

		System.out.println("element que més es repeteix: " + mas);
		System.out.println("********************************");
		System.out.println(Arrays.toString(llista));
		System.out.println(Arrays.toString(vector));

		System.out.println("Cromos comuns:");
		System.out.println(cromosComunes(llista, vector));

	}

	public static String[] añadir(String[] llista, String nom) {

		String[] aux = new String[llista.length + 1];
		boolean añadido = false;

		for (int i = 0, j = 0; i < aux.length; i++) {

			if (!añadido && llista[j].compareTo(nom) >= 0) {
				aux[i] = nom;
				añadido = true;
			} else {
				aux[i] = llista[j];
				j++;
			}
		}
		if (!añadido) {
			aux[aux.length - 1] = nom;
		}
		return aux;
	}

	public static String masRepetido(String[] llista) {
		int num = 0, maxim = 0;
		String rep = llista[0];
		String nom = "";
		for (int i = 1; i < llista.length; i++) {
			if (llista[i].equals(rep)) {
				num++;
				if (num >= maxim) {
					maxim = num;
					nom = llista[i];
				}
			} else {
				num = 0;
			}
			rep = llista[i];
		}
		return nom;

	}

	public static int cromosComunes(String[] llista, String[] vector) {
		int rep = 0;
		int i = 0, j = 0;
		while (i < llista.length && j < vector.length) {
			int eq = llista[i].compareTo(vector[j]);
			if (eq == 0) {
				rep++;
				i++;
				j++;
			} else if (eq < 0) {
				i++;
			} else {
				j++;
			}
		}
		return rep;
	}

}

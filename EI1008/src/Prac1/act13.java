package Prac1;

public class act13 {

	public static void main(String[] args) {
		String cadena = " casa roja coche verde";
		System.out.println(contarPalabras(cadena, 2));
	}

	public static String contarPalabras(String cadena, int n) {
		int num = cadena.length(), palabra = 0;
		String paraula = null;
		int inici = 0, fi = 0;
		char anterior = ' ';
		for (int i = 0; i < num - 1; i++) {

			if (cadena.charAt(i) != ' ' && anterior == ' ') {
				palabra++;
				if (palabra == n) {
					inici = i;
				}
				if (palabra == n + 1) {
					fi = i;
				}
			}
			anterior = cadena.charAt(i);
		}

		if (cadena.charAt(num - 1) != ' ')
			palabra++;
		if (palabra == n + 1) {
			fi = cadena.length();
		}
		
		if (fi > 0)
			return paraula = cadena.substring(inici, fi);
		else
			return paraula;

	}

}

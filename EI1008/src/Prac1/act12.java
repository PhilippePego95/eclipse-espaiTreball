//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

public class act12 {

	public static void main(String[] args) {
		System.out.println(contarPalabras(" hola  que tal estan ustedes bien i tu?"));

	}

	public static int contarPalabras(String cadena) {
		int num = cadena.length(), palabra = 0;
		String espai = " ";
		for (int i = 0; i < num - 1; i++) {
			if (cadena.charAt(i) != espai.charAt(0) && cadena.charAt(i + 1) == espai.charAt(0)) {
				palabra++;
			}
		}
		if (cadena.charAt(num - 1) != espai.charAt(0))
			palabra++;
		return palabra;
	}
}

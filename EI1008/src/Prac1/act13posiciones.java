//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

public class act13posiciones {
	public static void main(String[] args) {
		
		System.out.println(obtenerPalabra(" hola que tal estan ustedes", 1));

	}

	public static String obtenerPalabra(String cadena, int num) {
		
		int principi = 0, fi = 0;
		boolean inici = true;
		boolean fin = true;
		
		if (cadena.length() <= num || cadena.charAt(num) == ' ') {
			return null;
		} else {
			for (int i = 0; i <= cadena.length() - 1; i++) {
				if (inici == true && num - i >= 0 && cadena.charAt(num - i) == ' ') {
					principi = num - i + 1;
					inici = false;
				}
				if (fin == true && (num + i < cadena.length() || cadena.charAt(num + i) == ' ')) {
					fi = num + i + 1;
					if (num + i + 1 == cadena.length() || cadena.charAt(num + i) == ' ') {
						fin = false;
					}
				}
			}
			return (cadena.substring(principi, fi));

		}

	}
}

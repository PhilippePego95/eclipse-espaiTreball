package practica4.part1;

public class act02 {
	public static void main(String[] args) {
		permutaciones(4);
	}

	public static void permutaciones(int n) {
		int[] disponibles = new int[n];
		// Rellenar disponibles
		for (int i = 0; i < n; i++)
			disponibles[i] = i + 1;

		permutaciones(disponibles, "");

	}

	private static void permutaciones(int[] disponibles, String prefijo) {
		if (disponibles.length == 0) { // Caso base: escribir el prefijo
			System.out.println(prefijo);
		} else { // Caso general
			int[] auxiliar = new int[disponibles.length - 1];
			for (int e : disponibles) {
				for (int i = 0, j = 0; i < disponibles.length; i++) {
					if (disponibles[i] != e) {
						auxiliar[j++] = disponibles[i];
					}
				}
				permutaciones(auxiliar, prefijo + e);
			}
		}

	}

}

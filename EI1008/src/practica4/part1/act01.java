package practica4.part1;

public class act01 {
	public static void main(String[] args) {
	
			variacionesRepetición(4, 4);
	}

	public static void variacionesRepetición(int n, int m) {
		variacionesRepetición(n, m, "");
	}

	private static void variacionesRepetición(int n, int m, String prefijo) {
		if (m == 0)  // Caso base: escribir el prefijo
			System.out.println(prefijo);
	    else // Caso general:
			for (int i = 1; i <= n; i++)
				variacionesRepetición(n, m - 1, prefijo + i);

		
	}

}

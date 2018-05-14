package Prac1;

public class j23 {

	public static void main(String[] args) {
		int[][]matriz= {{1,2,3,4,1},
						{1,1,3,1,5},
						{1,2,1,4,5}};
		
		System.out.println(estáEnTodasLasColumnas(matriz,7));
	}

	public static boolean estáEnTodasLasColumnas(int[][] matriu, int numero) {
		boolean esta = true;

		for (int j = 0; j < matriu[0].length; j++) {

			esta = false;
			for (int i = 0; i < matriu.length; i++) {
				if (matriu[i][j] == numero) {
					esta = true;
				}
			}
			if (esta == false) {
				return false;
			}
		}

		return true;
	}

}

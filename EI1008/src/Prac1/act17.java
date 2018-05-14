//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

public class act17 {

	public static void main(String[] args) {
		int[]vector= {1,2,3,4,4};
		System.out.println(hayRepetidos(vector));

		
	}
	public static boolean hayRepetidos(int[]vector) {
		int cont;
		for(int i=0;i<vector.length;i++) {
			cont=0;
			for(int j=0;j<vector.length;j++) {
				if(vector[i]==vector[j]) {
					cont++;
				}
				if (cont>1)
					return true;
				
			}	
		}
		return false;
	}

}

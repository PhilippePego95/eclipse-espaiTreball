//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

public class act21 {

	public static void main(String[] args) {
		int[] vector = { -5, 2, 4, 5, 7, 9, 12 };
		System.out.println(posiciónInserción(vector, 4));
	}

	public static int posiciónInserción(int[] vector, int num) {
		for (int i = 0; i < vector.length - 1; i++) {
			if (vector[i] == num) {
				return i;
			} else {
				if (vector[i] < num && num < vector[i + 1]) {
					return i + 1;
				}
			}
		}if(vector[vector.length-1]<num) {
			return vector.length;
		}
		
		return -1;
	}

}

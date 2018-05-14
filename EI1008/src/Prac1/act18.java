//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

import java.util.Arrays;

public class act18 {

	public static void main(String[] args) {
		int[]vector= {0,1,2,3,4,5,6,7,8,7};
		System.out.println(Arrays.toString(vector));

		vector=eliminarPosición(vector,1);
		System.out.println(Arrays.toString(vector));


	}

	public static int[] eliminarPosición(int[] vector, int pos) {
		if (pos >= vector.length) {
			return vector;
		} else {
			int[] nouVector = new int[vector.length - 1];
			int j=0;
			for (int i = 0; i < vector.length; i++) {
				if (i != pos) {
					nouVector[j] = vector[i];
					j++;
				}
			}
			return nouVector;
		}
	}

}

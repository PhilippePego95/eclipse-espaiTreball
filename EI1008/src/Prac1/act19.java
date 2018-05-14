//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

import java.util.Arrays;

public class act19 {

	public static void main(String[] args) {
		
		int[]vector= {0,1,5,4,5,5,5,8,9};
		System.out.println(Arrays.toString(vector));

		vector=eliminarValor(vector,5);
		System.out.println(Arrays.toString(vector));

		/*for(int i=0;i<vector.length;i++) {
			System.out.print(vector[i]+" ");
		}*/

	}
	public static int[] eliminarValor(int[] vector,int num) {
		int n=0;
		for (int i=0;i<vector.length;i++) {
			if(vector[i]==num) {
				n++;
			}
		}
		if (n==0) {
			return vector;
		}
		int[]nouVector=new int[vector.length-n];
		int j=0;
		for(int i=0;i<vector.length;i++) {
			if(vector[i]!=num) {
				nouVector[j]=vector[i];
				j++;
			}
		}
		
		return nouVector;
	}

}

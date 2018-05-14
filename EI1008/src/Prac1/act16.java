//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

public class act16 {

	public static void main(String[] args) {
		double[] vector= {1,2,0,-9,-8,-7,-1,0,2,1,0,-1,-2,-3,-2,-2,1};
		System.out.println(contarOlasDeFrío(vector,3));
	}
	public static int contarOlasDeFrío(double[]vector,int n) {
		int cont=0,ola=0;
		for(int i=0; i<vector.length;i++) {
			if(vector[i]<0) {
				cont++;
			}else {
				if (cont>n) {
					ola++;
				}
				cont=0;
			}			
		}
		if (cont>n) {
			ola++;
		}
		return ola;
	}

}

package Prac1;

public class j14 {

	public static void main(String[] args) {
		int[] vector= {1,2,3,4,4,5};
		System.out.println( últimaPosición(vector,4));
	}
	public static int  últimaPosición(int[]vector,int numero) {
		int posicion=-2;
		
		for(int i=0; i<vector.length;i++) {
			if(vector[i]==numero) {
				posicion=i;
			}
		}
		
		return posicion;
	}
}

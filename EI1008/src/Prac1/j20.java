package Prac1;

public class j20 {

	public static void main(String[] args) {
		int[]v1= {1,3,4,6};
		int []v2= {1,3};
		System.out.println(contiene(v1,v2));
		
	
	}
	public static boolean contiene(int []vector,int numero) {
		for (int i=0; i<vector.length;i++) {
			if (vector[i]==numero) {
				return true;
			}
		}
		return false;
	}
	
	public static boolean contiene(int []vector,int []vector1) {
		for (int i=0;i<vector1.length;i++) {
			if(contiene(vector,vector1[i])==false) {
				return false;
			}
			
		}
		return true;
		
	}

	
}

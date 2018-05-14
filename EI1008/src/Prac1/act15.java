//Practica 1 			Programació II			Philippe Gonzalez i Alejandro Mir

package Prac1;

public class act15 {

	public static void main(String[] args) {
		String[]vector= {"alejandri","jose","phil","ximo"};
		System.out.println(estáOrdenado(vector));

	}
	public static boolean estáOrdenado(String[] vector) {
		for(int i=1;i<vector.length;i++) {
			if(vector[i-1].compareTo(vector[i])>0){
				return false;
			}
		}
		return true;
	}

}

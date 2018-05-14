package practica2.ejercicio01;

public class Act01 {

	public static void main(String[] args) {
		
		Punto punt=new Punto(3.5,4.25);
		System.out.println("Punt1: "+punt.toString());
		System.out.println("X: "+punt.getX());
		System.out.println("Y: "+punt.getY());
		Punto punt2= new Punto(3.5,1.25);
		System.out.println("Punt2: "+punt2.toString());

		//System.out.println(punt.toString());
		
		System.out.println("Distancia: "+punt.distancia(punt2));
		System.out.println("Comparar: "+punt.equals(punt2));
	}

}

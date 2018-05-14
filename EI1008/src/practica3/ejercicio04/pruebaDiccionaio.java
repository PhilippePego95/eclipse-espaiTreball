package practica3.ejercicio04;

public class pruebaDiccionaio {
	public static void main(String[]args) {
		Diccionario dic =new Diccionario();
		System.out.println(dic);

		dic.añadir("hola", 1);
		System.out.println(dic);
		dic.añadir("hadeu", 1);	dic.añadir("haxasa", 1);	dic.añadir("roja", 1);
		System.out.println(dic);
		
		dic.añadir("hadeu", 1);	dic.añadir("haxasa", 1);	dic.añadir("roja", 1);	dic.añadir("vroja", 1);
		System.out.println(dic);
	//	dic.añadir("roja", 1);
		System.out.println("hola ->>"+dic.cantidad("hola"));
		System.out.println("Cadena con mayor cantidad: "+dic.cadenaConMayorCantidad());
		dic.quitar("roja",2);
		System.out.println(dic);

	}
}

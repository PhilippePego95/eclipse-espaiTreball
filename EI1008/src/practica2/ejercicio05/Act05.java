package practica2.ejercicio05;

public class Act05 {

	public static void main(String[] args) {
		System.out.println(Fecha.añoBisiesto(1904));
		System.out.println(Fecha.díaMes(4, 2056));
		System.out.println(Fecha.hoy().toString());
		Fecha data = new Fecha(3, 5, 1807);
		Fecha data1 = new Fecha(2, 5, 1808);

		System.out.println(data.toString());
		System.out.println(data.díaSiguiente().toString());
		System.out.println("***");
		System.out.println(data.compareTo(data1));

	}
}

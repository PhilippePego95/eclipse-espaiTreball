package practica2.ejercicio10;


public class Tarea {
	private Fecha fecha;
	private String descripción;

	public Tarea(Fecha data,String descripció) {
		fecha=data;
		descripción=descripció;
	}


	public Fecha getFecha() {
		return fecha;
	}
	public String getDescripción() {
		return descripción;
	}
	
	public String toString() {
		return fecha+": "+descripción;
	}
}

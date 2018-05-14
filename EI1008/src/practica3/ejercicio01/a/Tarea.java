package practica3.ejercicio01.a;

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

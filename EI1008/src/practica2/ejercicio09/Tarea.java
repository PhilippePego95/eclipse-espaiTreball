package practica2.ejercicio09;


//Alejandro Mir Belert i Philippe Gonzalez Miralles
//Se ha utilizado la clase Fecha con la ExcepcionFechaInvalida

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

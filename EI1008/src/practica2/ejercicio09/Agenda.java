package practica2.ejercicio09;
//Alejandro Mir Belert i Philippe Gonzalez Miralles
//Se ha utilizado la clase Fecha con la ExcepcionFechaInvalida
public class Agenda {

	private Tarea[] vector;

	public Agenda() {
		vector = new Tarea[0];
	}

	public void añadir(Tarea tarea) {
		Tarea[] aux = new Tarea[vector.length + 1];
		boolean añadido = false;
		for (int i = 0, j = 0; i <= vector.length; i++) {
			if (!añadido && (i == vector.length || vector[j].getFecha().compareTo(tarea.getFecha()) > 0)) {
				aux[i] = tarea;
				añadido = true;
			} else {
				aux[i] = vector[j];
				j++;
			}
		}
		vector = aux;
	}

	public int cantidad() {
		return vector.length;
	}

	public String toString() {
		String cadena = "";
		for (int i = 0; i < cantidad(); i++) {
			cadena = cadena + vector[i].toString() + "\n";
		}
		return cadena;
	}

	public Tarea[] consultar(Fecha fecha) {
		int num = 0;
		for (int i = 0; i < cantidad(); i++) {
			if (vector[i].getFecha().compareTo(fecha) == 0)
				num++;
		}
		Tarea[] consulta = new Tarea[num];

		for (int i = 0, j = 0; i < cantidad(); i++) {
			if (vector[i].getFecha().compareTo(fecha) == 0) {
				consulta[j] = vector[i];
				j++;
			}
		}
		return consulta;

	}

	public void borrarPasadas(Fecha fecha) {
		int num = 0;
		for (int i = 0; i < cantidad(); i++) {
			if (vector[i].getFecha().compareTo(fecha) < 0)
				num++;

		}
		Tarea[] aux = new Tarea[cantidad() - num];
		for (int i = 0, j = 0; i < cantidad(); i++) {
			if (vector[i].getFecha().compareTo(fecha) >= 0) {
				aux[j] = vector[i];
				j++;
			}
		}
		vector = aux;

	}

	public void borrar() throws ExcepcionFechaInvalida {
		borrarPasadas(Fecha.hoy());
	}

}

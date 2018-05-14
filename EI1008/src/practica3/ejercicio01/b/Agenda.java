package practica3.ejercicio01.b;

import java.util.LinkedList;


public class Agenda {
	private  LinkedList< Tarea > lista = new LinkedList< Tarea >();
	
	
	public void añadir(Tarea tarea) {
		LinkedList< Tarea > aux = new LinkedList< Tarea >();		
		boolean añadido = false;
		for (int i = 0, j = 0; i <= cantidad(); i++) {
			if (!añadido && (i == cantidad() || lista.get(j).getFecha().compareTo(tarea.getFecha()) > 0)) {
				aux.add(i,tarea);
				añadido = true;
			} else {
				aux.add(i,lista.get(j));
				j++;
			}
		}
		lista = aux;
	}

	public int cantidad() {
		return lista.size();
	}
	public String toString() {
		String cadena = "";
		for (int i = 0; i < cantidad(); i++) {
			cadena = cadena + lista.get(i) + "\n";
		}
		return cadena;
	}
	public Tarea[] consultar(Fecha fecha) {
		int num = 0;
		for (int i = 0; i < cantidad(); i++) {
			if (lista.get(i).getFecha().compareTo(fecha) == 0)
				num++;
		}
		Tarea[] consulta = new Tarea[num];

		for (int i = 0, j = 0; i < cantidad(); i++) {
			if (lista.get(i).getFecha().compareTo(fecha) == 0) {
				consulta[j] = lista.get(i);
				j++;
			}
		}
		return consulta;

	}
	public void borrarPasadas(Fecha fecha) {
		for (int i = 0; i < cantidad();) {

			if (lista.get(i).getFecha().compareTo(fecha) < 0) {

				lista.remove(i);

			} else {
				i++;
			}

		}
	}
	public void borrar() throws ExcepcionFechaInvalida {
		borrarPasadas(Fecha.hoy());
	}
	

}
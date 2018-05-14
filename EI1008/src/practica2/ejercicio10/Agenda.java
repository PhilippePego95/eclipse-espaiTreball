package practica2.ejercicio10;

public class Agenda {

	private static final int TAMAÑO_INICIAL = 8;
	private Tarea[] vector;
	private int cantidad;

	public Agenda() {
		vector  = new Tarea[TAMAÑO_INICIAL];
		cantidad  = 0;
	}

	public void añadir(Tarea tarea) {
		cantidad++;

		if (cantidad < vector.length) {
			Tarea aux;
			for (int i = 0; i < cantidad - 1; i++) {
				if (vector[i].getFecha().compareTo(tarea.getFecha()) > 0) {
					aux = vector[i];
					vector[i] = tarea;
					tarea = aux;
				}
			}
			vector[cantidad - 1] = tarea;
		} else {

			Tarea[] aux = new Tarea[vector.length * 2];
			boolean añadido = false;
			for (int i = 0, j = 0; i < cantidad; i++) {
				if (!añadido && (i == cantidad - 1 || vector[j].getFecha().compareTo(tarea.getFecha()) > 0)) {
					aux[i] = tarea;
					añadido = true;
				} else {
					aux[i] = vector[j];
					j++;
				}

			}
			vector = aux;
		}
	}

	public int cantidad() {
		return cantidad;
	}

	public String toString() {
		String cadena = "";
		for (int i = 0; i < cantidad; i++) {
			cadena = cadena + vector[i] + "\n";
		}
		return cadena;
	}

	public Tarea[] consultar(Fecha fecha) {
		int num = 0;
		for (int i = 0; i < cantidad; i++) {
			if (vector[i].getFecha().compareTo(fecha) == 0)
				num++;
		}
		Tarea[] consulta = new Tarea[num];

		for (int i = 0, j = 0; i < cantidad; i++) {
			if (vector[i].getFecha().compareTo(fecha) == 0) {

				consulta[j] = vector[i];
				j++;

			}
		}
		return consulta;

	}

	public void borrarPasadas(Fecha fecha) {
		boolean primer = false;
		int n = 0, prim = 0, ultim = 0;
		for (int i = 0; i < cantidad; i++) {
			if (vector[i].getFecha().compareTo(fecha) < 0) {
				ultim = i;
				if (primer)
					prim = i;
				n++;
				vector[i] = null;
			}
		}

		for (int i = prim; i < cantidad; i++) {
			ultim++;
			vector[i] = vector[ultim];

		}
		cantidad = cantidad - n;

		if(cantidad<=vector.length/4) {
			reducir();
		}
			

	}

	public void borrar() throws ExcepcionFechaInvalida {
		borrarPasadas(Fecha.hoy());
	}

	
	private void reducir() {
		Tarea[] nou=new Tarea[vector.length/2];
		for(int i=0;i<cantidad;i++) {
			nou[i]=vector[i];
		}
		vector=nou;
		
	}
}

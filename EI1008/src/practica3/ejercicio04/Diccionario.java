package practica3.ejercicio04;

public class Diccionario {

	private Nodo primero;
	private Nodo ultimo;

	int talla;

	private class Nodo {
		String dato;
		int cantidad;
		Nodo sig;
		Nodo ant;

		public Nodo(String dato, int n) {
			this.dato = dato;
			this.cantidad = n;
		}

	}

	public boolean isEmpty() {
		return talla == 0;
	}

	public String toString() {
		if (talla > 0) {
			String cadena = "{";

			Nodo aux;
			for (aux = primero; aux.sig != null; aux = aux.sig) {
				cadena = cadena + aux.dato + "-->" + aux.cantidad + ", ";

			}

			return cadena + aux.dato + "-->" + aux.cantidad + "}";
		}
		return "{}";

	}

	public int cantidad(String unaCadena) {
		Nodo aux;
		for (aux = primero; aux != null; aux = aux.sig) {
			if (aux.dato.equals(unaCadena)) {
				return aux.cantidad;
			}
		}
		return 0;
	}

	public String cadenaConMayorCantidad() {
		Nodo aux;
		String cadena = null;
		int maxim = 0;
		for (aux = primero; aux != null; aux = aux.sig) {
			if (aux.cantidad >= maxim) {
				maxim = aux.cantidad;
				cadena = aux.dato;
			}
		}
		return cadena;
	}

	public void añadir(String unaCadena, int unaCantidad) {
		// System.out.println(".");
		if (isEmpty()) {
			Nodo node = new Nodo(unaCadena, unaCantidad);
			primero = ultimo = node;
			talla++;
		} else {
			Nodo aux = primero;
			boolean añadido = false;
			Nodo node = new Nodo(unaCadena, unaCantidad);
			for (int i = 0; i < talla; i++) {
				int res=aux.dato.compareTo(unaCadena);
				if (res == 0) {
					aux.cantidad += unaCantidad;
					añadido = true;
					break;
				} else if (res > 0) {
					if (i > 0) {
						aux.ant.sig = node;
						node.ant = aux.ant;
						node.sig = aux;
						aux.ant = node;
						if (i == talla) {
							ultimo = node;
						}
						añadido = true;
					} else if (i == 0) {
						node.sig = primero;
						primero.ant = node;
						primero = node;
						añadido = true;
					}
					talla++;

					break;
				}
				aux = aux.sig;
			}
			if (!añadido) {
				ultimo.sig = node;
				node.ant = ultimo;
				ultimo = node;
				talla++;
			}

		}
	}

	public void quitar(String unaCadena, int unaCantidad) {
		Nodo aux = primero;
		for (int i = 0; i < talla; i++) {
			if (aux.dato.compareTo(unaCadena) == 0) {
				aux.cantidad -= unaCantidad;
				if (aux.cantidad == 0) {
					if (i == 0) {
						if (talla == 1) {
							primero = ultimo = null;
						} else {
							primero = aux.sig;
							primero.ant = null;

						}
					} else if (i == talla - 1) {
						ultimo = aux.ant;
						ultimo.sig = null;
					} else {
						aux.ant.sig = aux.sig;
						aux.sig.ant = aux.ant;

					}
				}
				break;
			}
			if (aux.dato.compareTo(unaCadena) > 0) {
				break;
			}
			aux = aux.sig;
		}
	}

}
package practica3.ejercicio02;

public class ListaCadenasEnlaceDoble implements ListaCadenas {
	private Nodo primero;
	private Nodo ultimo;

	int talla;

	private class Nodo {
		String dato;
		Nodo sig;
		Nodo ant;

		public Nodo(String dato) {
			this.dato = dato;
		}

	}

	@Override
	public boolean add(String s) {
		if (talla == 0) {
			primero = ultimo = new Nodo(s);
		} else {
			Nodo aux = new Nodo(s);
			ultimo.sig = aux;
			aux.ant = ultimo;
			ultimo = aux;
		}
		talla++;
		return true;
	}

	@Override
	public void add(int i, String s) {
		if ( i < 0||i > size())
			throw new IndexOutOfBoundsException();
		Nodo nou = new Nodo(s);
		
		if(talla==0) {
			primero = ultimo = new Nodo(s);

		}else if (i == 0) {
			nou.sig = primero;
			primero.ant = nou;
			primero = nou;

		} else if (i == talla) {
			ultimo.sig = nou;
			nou.ant = ultimo;
			ultimo = nou;

		} else {
			Nodo aux;
			if (i < talla / 2) {
				aux = primero;
				for (int pos = 0; pos < i; pos++) {
					aux = aux.sig;
				}

			} else {
				aux = ultimo;
				for (int pos = talla - 1; pos > i; pos--) {
					aux = aux.ant;
				}

				aux.ant.sig = nou;
				nou.ant = aux.ant;

				nou.sig = aux;
				aux.ant = nou;

			}
		}
		talla++;

	}

	@Override
	public void clear() {
		primero = null;
		ultimo = null;
		talla = 0;
	}

	@Override
	public String get(int i) {
		if (i >= size() || i < 0)
			throw new IndexOutOfBoundsException();
		Nodo aux;
		if (i < talla / 2) {
			aux = primero;
			for (int pos = 0; pos < i; pos++) {
				aux = aux.sig;
			}

		} else {
			aux = ultimo;
			for (int pos = talla - 1; pos > i; pos--) {
				aux = aux.ant;
			}
		}
		return aux.dato;
	}

	@Override
	public int indexOf(String s) {
		Nodo aux = primero;
		for (int pos = 0; pos < talla; pos++) {
			if (aux.dato.equals(s)) {
				return pos;
			}
			aux = aux.sig;

		}
		return -1;
	}

	@Override
	public int lastIndexOf(String s) {
		Nodo aux = ultimo;
		for (int i = talla - 1; i >= 0; i--) {
			if (aux.dato.equals(s)) {
				return i;
			}
			aux = aux.ant;
		}
		return -1;
	}

	@Override
	public boolean isEmpty() {
		return primero == null;
	}

	@Override
	public String remove(int i) {
		if (i >= size() || i < 0)
			throw new IndexOutOfBoundsException();
		Nodo aux;
		if (i == 0) {
			String cadena = primero.dato;
			primero.ant = null;

			primero = primero.sig;
			talla--;
			return cadena;
		} else if (i == talla - 1) {
			String cadena = ultimo.dato;
			ultimo.ant.sig = null;
			ultimo = ultimo.ant;
			talla--;
			return cadena;

		}

		if (i < talla / 2) {
			aux = primero;
			for (int pos = 0; pos < i; pos++) {
				aux = aux.sig;
			}

		} else {
			aux = ultimo;
			for (int pos = talla - 1; pos > i; pos--) {
				aux = aux.ant;
			}
		}
		String cadena = aux.dato;
		aux.ant.sig = aux.sig;
		aux.sig.ant = aux.ant;
		talla--;
		return cadena;
	}

	@Override
	public boolean remove(String s) {
		int pos=indexOf(s);

		if(pos>-1) {
			remove(pos);
			return true;
		}
		return false;
	
	}

	@Override
	public String set(int i, String s) {
		if (i >= size() || i < 0)
			throw new IndexOutOfBoundsException();
		Nodo aux;
		if (i < talla / 2) {
			aux = primero;
			for (int pos = 0; pos < i; pos++) {
				aux = aux.sig;
			}

		} else {
			aux = ultimo;
			for (int pos = talla - 1; pos > i; pos--) {
				aux = aux.ant;
			}
		}
		String cadena = aux.dato;
		aux.dato = s;
		return cadena;
	}

	@Override
	public int size() {
		return talla;
	}

	public String toString() {
		if (talla > 0) {
			String cadena = "[";

			Nodo aux;
			for (aux = primero; aux.sig != null; aux = aux.sig) {
				cadena = cadena + aux.dato + ", ";

			}

			return cadena + aux.dato + "]";
		}
		return "[]";

	}

}

package practica3.ejercicio02;

public class ListaCadenasEnlaceSimple implements ListaCadenas {
	private Nodo primero;
	int talla;

	private class Nodo {
		String dato;
		Nodo sig;

		public Nodo(String dato) {
			this.dato = dato;
		}

	}

	public boolean add(String s) {
		talla++;
		Nodo nou = new Nodo(s);
		if (isEmpty()) {
			primero = nou;
		} else {
			Nodo aux;
			for (aux = primero; aux.sig != null; aux = aux.sig) {
				;
			}
			aux.sig = nou;
		}

		return true;

	}

	public boolean ifaddString(String s) {// metode del tercer control
		if (talla == 0) {
			primero = new Nodo(s);
			talla++;
			return true;
		}
		Nodo aux = primero;
		for (int i = 0; i < talla-1; i++) {
			if (aux.dato.equals(s)) {
				return false;
			}
			aux = aux.sig;
		}
		Nodo node = new Nodo(s);
		aux.sig = node;
		talla++;
		return true;
	}

	@Override
	public void add(int i, String s) {

		if (i > size() || i < 0)
			throw new IndexOutOfBoundsException();

		Nodo aux = primero, nou = new Nodo(s);

		if (i == 0) {
			nou.sig = primero;
			primero = nou;
		} else {

			int j = 0;
			for (aux = primero; aux != null; aux = aux.sig) {
				if (i - 1 == j) {
					nou.sig = aux.sig;
					aux.sig = nou;
					break;
				}
				j++;
			}
		}
		talla++;

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

	@Override
	public void clear() {
		primero = null;
		talla = 0;
	}

	@Override
	public String get(int i) {
		if (i >= size() || i < 0)
			throw new IndexOutOfBoundsException();

		Nodo aux = primero;
		for (int pos = 0; pos < i; pos++) {
			aux = aux.sig;

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
		Nodo aux = primero;
		int fin = -1;
		for (int pos = 0; pos < talla; pos++) {
			if (aux.dato.equals(s)) {
				fin = pos;
			}
			aux = aux.sig;

		}
		return fin;
	}

	@Override
	public boolean isEmpty() {
		return primero == null;
	}

	@Override
	public String remove(int i) {
		if (i >= size() || i < 0)
			throw new IndexOutOfBoundsException();

		Nodo aux = primero;
		String cadena = null;
		if (i == 0) {
			cadena = primero.dato;
			primero = primero.sig;
			talla--;
		} else {
			for (int pos = 0; pos < i - 1; pos++) {
				aux = aux.sig;
			}
			cadena = aux.sig.dato;
			aux.sig = aux.sig.sig;
			talla--;
		}

		return cadena;
	}

	@Override
	public boolean remove(String s) {

		int pos = indexOf(s);

		if (pos > -1) {
			remove(pos);
			return true;
		}
		return false;
	}

	@Override
	public String set(int i, String s) {
		if (i >= size() || i < 0)
			throw new IndexOutOfBoundsException();
		Nodo aux = primero;
		for (int pos = 0; pos < i; pos++) {
			aux = aux.sig;
		}
		String cadena = aux.dato;
		aux.dato = s;

		return cadena;
	}

	@Override
	public int size() {
		return talla;
	}

}

package practica2.ejercicio05;

import java.util.Calendar;

//Alejandro Mir Belert i Philippe Gonzalez Miralles
public class Fecha {
	private int día;
	private int mes;
	private int año;

	public Fecha(int dia, int mess, int any) {
		día = dia;
		mes = mess;
		año = any;
	}

	public Fecha(Fecha fecha) {
		día = fecha.día;
		mes = fecha.mes;
		año = fecha.año;
	}

	public int getDía() {
		return día;
	}

	public int getMes() {
		return mes;
	}

	public int getAño() {
		return año;
	}

	public static Fecha hoy() {
		Calendar calendario = Calendar.getInstance();
		int día = calendario.get(Calendar.DAY_OF_MONTH);
		int mes = calendario.get(Calendar.MONTH) + 1;
		int año = calendario.get(Calendar.YEAR);
		return new Fecha(día, mes, año);
	}

	public static boolean añoBisiesto(int año) {

		if (año % 4 == 0 && (año % 400 == 0 || año %100!=0)) {
			return true;
		}
		return false;
	}

	public static int díaMes(int mes, int año) {
		if (mes == 1 || mes == 3 || mes == 5 || mes == 7 || mes == 8 || mes == 10 || mes == 12) {
			return 31;
		} else if (mes == 4 || mes == 6 || mes == 9 || mes == 11) {
			return 30;
		} else if (Fecha.añoBisiesto(año)) {
			return 29;
		}
		return 28;
	}

	public String toString() {
		return día + "/" + mes + "/" + año;
	}

	public boolean equals(Object otroObjeto) {
		if (this == otroObjeto)
			return true;
		if (!(otroObjeto instanceof Fecha))
			return false;
		Fecha otraFecha = (Fecha) otroObjeto;
		return día == otraFecha.día && mes == otraFecha.mes && año == otraFecha.año;
	}

	public int compareTo(Fecha otraFecha) {
		if (this.equals(otraFecha)) {
			return 0;
		} else if (año >otraFecha.año) {
			return 1;
		} else if (mes > otraFecha.mes && año ==otraFecha.año) {
			return 1;
		} else if (día > otraFecha.día && mes == otraFecha.mes && año ==otraFecha.año) {
			return 1;
		}
		return -1;

	}

	public Fecha díaSiguiente() {
		if (día + 1 > díaMes(mes, año) && mes + 1 <= 12) {
			return new Fecha(1, this.mes + 1, año);
		} else if (this.día + 1 > díaMes(this.mes, año) && mes + 1 > 12) {
			return new Fecha(1, 1, año + 1);
		}
		return new Fecha(día + 1, mes, año);

	}
}

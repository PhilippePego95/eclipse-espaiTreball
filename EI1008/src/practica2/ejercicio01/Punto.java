package practica2.ejercicio01;

import java.util.Locale;

public class Punto {
	private double x;
	private double y;

	public Punto(double puntX, double puntY) {
		x = puntX;
		y = puntY;
	}

	public Punto() {
		x = 0;
		y = 0;
	}

	public double getX() {
		return x;
	}

	public double getY() {
		return y;
	}

	public Object desplazar(double desplazamientoX, double desplazamientoY) {
		return new Punto(x + desplazamientoX, y + desplazamientoY);
		//return puntoDesplazado;
	}

	public double distancia(Punto otroPunto) {
		//double x1 = getX();
		double x2 = otroPunto.x;
		//double y1 = getY();
		double y2 = otroPunto.y;

	//	double resultat = Math.sqrt(Math.pow(x2 - x, 2) + Math.pow(y2 - y, 2));
		return Math.sqrt(Math.pow(x2 - x, 2) + Math.pow(y2 - y, 2));//resultat;

	}

	public String toString() {

		return String.format(Locale.UK,"(%.2f, %.2f)",x,y);
				//"(" + x + "," + y + ")";
		
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!(obj instanceof Punto))
			return false;
		Punto otraPunto = (Punto) obj;
		return x == otraPunto.x && y == otraPunto.y;
	}

}

package practica4.part2;

import es.uji.dlsi.eimt1008.cronometrador.Resolvedor;

public class TodosIgualesOrdenado implements Resolvedor<Boolean>{
	public Boolean resuelve(int[] vector) {
		if(vector[0]==vector[vector.length-1])
		return true;
		
		return false;
	}
}

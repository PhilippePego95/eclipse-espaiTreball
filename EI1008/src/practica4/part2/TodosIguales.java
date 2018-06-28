package practica4.part2;

import es.uji.dlsi.eimt1008.cronometrador.Resolvedor;

public class TodosIguales implements Resolvedor<Boolean>{

	@Override
	public Boolean resuelve(int[] vector) {
		for (int i=1;i<vector.length;i++)
			if(vector[0]!=vector[i])
				return false;
		return true;
	}
	

}

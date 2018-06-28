package practica4.part2;

import es.uji.dlsi.eimt1008.cronometrador.Resolvedor;

public class EncuentraMayor implements Resolvedor<Integer>{

	@Override
	public Integer resuelve(int[] vector) {
		int maxim= vector[0];
		for(int i=1;i<vector.length;i++) 
			if(vector[i]>maxim)
				maxim=vector[i];
		
		return maxim;
	}

}

package practica4.part2;

import es.uji.dlsi.eimt1008.cronometrador.Resolvedor;

public class TodosDistintosOrdenado implements Resolvedor<Boolean>{

	@Override
	public Boolean resuelve(int[] vec) {
		for(int i=0;i<vec.length;i++) {
			for(int j=i;j<vec.length;j++) {
				if(vec[i]==vec[j]) {
					return false;
				}
				if(vec[i]<vec[j])
					break;
			}

		}
		return true;
	
	}

}

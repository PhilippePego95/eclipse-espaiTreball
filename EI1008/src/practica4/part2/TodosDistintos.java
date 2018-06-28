package practica4.part2;

import es.uji.dlsi.eimt1008.cronometrador.Resolvedor;

public class TodosDistintos implements Resolvedor<Boolean>{

	@Override
	public Boolean resuelve(int[] vec) {
		for(int i=0;i<vec.length;i++) {
			for(int j=i;j<vec.length;j++) {
				if(vec[i]==vec[j]&& i!=j) {
					return false;
				}
			}

		}
		return true;
	}

}

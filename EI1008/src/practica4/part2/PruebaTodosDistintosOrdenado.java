package practica4.part2;

import static es.uji.dlsi.eimt1008.cronometrador.Generadores.con;
import static es.uji.dlsi.eimt1008.cronometrador.Generadores.generador;
import es.uji.dlsi.eimt1008.cronometrador.Cronometrador;
import es.uji.dlsi.eimt1008.cronometrador.Estadísticas;
import es.uji.dlsi.eimt1008.cronometrador.Generadores.VectorDistintos;
import es.uji.dlsi.eimt1008.cronometrador.Generadores.VectorIguales;
import es.uji.dlsi.eimt1008.cronometrador.Generadores.VectorUniforme;
import es.uji.dlsi.eimt1008.cronometrador.Grafico;

public class PruebaTodosDistintosOrdenado {
    public static void main(String[] args) {
        Cronometrador c = new Cronometrador();
        c.setTallaMáxima(10000);
        Estadísticas[] estadísticas = c.cronometra(new TodosDistintosOrdenado(),
                con(generador(new VectorUniforme(1000)).ordenaVector().hecho())
                .añadePeorCaso(generador(new VectorDistintos(100000000)).ordenaVector().hecho())
                .añadeMejorCaso(new VectorIguales(1000))
                .construye());
        Grafico gráfico = new Grafico("Todos distintos, vector ordenado");
        gráfico.añadeSerie(estadísticas, "Todos distintos");
        gráfico.muestra();

    }

}

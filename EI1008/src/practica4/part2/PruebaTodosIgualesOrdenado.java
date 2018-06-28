package practica4.part2;

import static es.uji.dlsi.eimt1008.cronometrador.Generadores.con;
import static es.uji.dlsi.eimt1008.cronometrador.Generadores.generador;
import es.uji.dlsi.eimt1008.cronometrador.Cronometrador;
import es.uji.dlsi.eimt1008.cronometrador.Estadísticas;
import es.uji.dlsi.eimt1008.cronometrador.Generadores.VectorDistintos;
import es.uji.dlsi.eimt1008.cronometrador.Generadores.VectorIguales;
import es.uji.dlsi.eimt1008.cronometrador.Generadores.VectorUniforme;
import es.uji.dlsi.eimt1008.cronometrador.Grafico;

public class PruebaTodosIgualesOrdenado {

    public static void main(String[] args) {
        Cronometrador c = new Cronometrador();
        c.setVirtuales(2000);
        Estadísticas[] estadísticas = c.cronometra(new TodosIgualesOrdenado(),
                con(generador(new VectorUniforme(1000)).ordenaVector().hecho())
                .añadeMejorCaso(generador(new VectorDistintos(100000000)).ordenaVector().hecho())
                .añadePeorCaso(new VectorIguales(1000))
                .construye());
        Grafico gráfico = new Grafico("Todos iguales, vector ordenado");
        gráfico.añadeSerie(estadísticas, "Todos iguales");
        gráfico.muestra();
    }

}

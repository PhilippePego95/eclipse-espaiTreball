package practica4.part2;

import static es.uji.dlsi.eimt1008.cronometrador.Generadores.con;
import es.uji.dlsi.eimt1008.cronometrador.Cronometrador;
import es.uji.dlsi.eimt1008.cronometrador.Estadísticas;
import es.uji.dlsi.eimt1008.cronometrador.Generadores.VectorDistintos;
import es.uji.dlsi.eimt1008.cronometrador.Generadores.VectorIguales;
import es.uji.dlsi.eimt1008.cronometrador.Generadores.VectorUniforme;
import es.uji.dlsi.eimt1008.cronometrador.Grafico;

public class PruebaTodosIguales {
    public static void main(String[] args) {
        Cronometrador c = new Cronometrador();
        Estadísticas[] estadísticas = c.cronometra(new TodosIguales(),
                con(new VectorUniforme(1000))
                .añadeMejorCaso(new VectorDistintos(100000000))
                .añadePeorCaso(new VectorIguales(1000))
                .construye());
        Grafico gráfico = new Grafico("Todos iguales");
        gráfico.añadeSerie(estadísticas, "Todos iguales");
        gráfico.muestra();
    }

}

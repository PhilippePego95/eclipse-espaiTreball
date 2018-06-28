package practica4.part2;

import static es.uji.dlsi.eimt1008.cronometrador.Generadores.con;
import es.uji.dlsi.eimt1008.cronometrador.Cronometrador;
import es.uji.dlsi.eimt1008.cronometrador.Estadísticas;
import es.uji.dlsi.eimt1008.cronometrador.Generadores.VectorUniforme;
import es.uji.dlsi.eimt1008.cronometrador.Grafico;

public class PruebaEncuentraMayor {
    public static void main(String[] args) {
        Cronometrador c = new Cronometrador();
        //c.setnPuntos(10);
        Estadísticas[] estadísticas = c.cronometra(new EncuentraMayor(), con(new VectorUniforme(1000)).construye());
        Grafico gráfico = new Grafico("Cálculo del Máximo");
        gráfico.añadeSerie(estadísticas, "Máximo");
        gráfico.muestra();
    }
}

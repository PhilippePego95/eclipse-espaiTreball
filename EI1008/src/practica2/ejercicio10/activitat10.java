package practica2.ejercicio10;

import java.util.Arrays;

public class activitat10 {

	public static void main(String[] args) throws ExcepcionFechaInvalida {
		Fecha fecha = new Fecha(15, 4, 2018);
		Fecha fecha2 = new Fecha(13, 4, 2018);
		Fecha fecha3 = new Fecha(20, 4, 2018);

		Tarea tarea = new Tarea(fecha, "Examen Mate ");
		Tarea tarea2 = new Tarea(fecha2, "Examen Fisica ");
		Tarea tarea3 = new Tarea(fecha3, "Examen Programació ");

		Agenda agenda = new Agenda();
		agenda.añadir(tarea2);
		agenda.añadir(tarea3);
		agenda.añadir(tarea);
		agenda.añadir(tarea);
		agenda.añadir(tarea);

		agenda.añadir(tarea);
		agenda.añadir(tarea2);
		agenda.añadir(tarea3);
	

		System.out.println(agenda.toString());

		System.out.println("Consulta");
		System.out.println(Arrays.toString(agenda.consultar(new Fecha(13, 4, 2018))));
		System.out.println("Borrar fechas pasadas: 14/04/2018");
		agenda.borrarPasadas(new Fecha(15, 4, 2018));
		System.out.println("Consulta 13, 4, 2018");
		System.out.println(Arrays.toString(agenda.consultar(new Fecha(13, 4, 2018))));

		System.out.println(agenda.toString());

		System.out.println("Borrar pasadas de hoy");
		agenda.borrar();
		System.out.println(agenda.toString());

	}

}

package practica3.ejercicio01.a;


public class activitat09 {

	public static void main(String[] args) throws ExcepcionFechaInvalida {
		Fecha fecha = new Fecha(15, 4, 2018);
		Fecha fecha2 = new Fecha(13, 4, 2018);
		Fecha fecha3 = new Fecha(24, 4, 2018);

		Tarea tarea = new Tarea(fecha, "Examen Mate ");
		Tarea tarea2 = new Tarea(fecha2, "Examen Fisica ");
		Tarea tarea3 = new Tarea(fecha3, "Examen Programació ");

		Agenda agenda = new Agenda();
		agenda.añadir(tarea);
		agenda.añadir(tarea2);
		agenda.añadir(tarea3);
		agenda.añadir(tarea);
		agenda.añadir(tarea);
		agenda.añadir(tarea2);
		agenda.añadir(tarea3);
		agenda.añadir(tarea);
		agenda.añadir(tarea);
		
		System.out.println(agenda.toString());
		System.out.println("Consulta");
		System.out.println(agenda.consultar(new Fecha(14, 4, 2018)));
		System.out.println("Borrar fechas pasadas: 14/04/2018");
		agenda.borrarPasadas(new Fecha(14, 4, 2018));
		System.out.println(agenda.toString());
		System.out.println("Borrar pasadas de hoy");
		agenda.borrar();
		System.out.println(agenda.toString());

	}

}

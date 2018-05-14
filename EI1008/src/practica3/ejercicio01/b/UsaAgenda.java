package practica3.ejercicio01.b;


public class UsaAgenda {

	public static void main(String[] args) throws ExcepcionFechaInvalida {
		Agenda agenda = new Agenda();
		
		System.out.println("Agenda con " + agenda.cantidad() + " tareas");
		System.out.println(agenda);
		
		agenda.añadir(new Tarea(new Fecha(16, 4, 2018), "EI1006"));
		System.out.println("Agenda con " + agenda.cantidad() + " tareas");
		System.out.println(agenda);

		agenda.añadir(new Tarea(new Fecha(26, 2, 2018), "EI1007-C1"));
		agenda.añadir(new Tarea(new Fecha(16, 4, 2018), "EI1007-C2"));
		agenda.añadir(new Tarea(new Fecha(7, 5, 2018), "EI1007-C3"));
		System.out.println("Agenda con " + agenda.cantidad() + " tareas");
		System.out.println(agenda);
		
		agenda.añadir(new Tarea(new Fecha(26, 3, 2018), "EI1008-C1"));
		agenda.añadir(new Tarea(new Fecha(23, 4, 2018), "EI1008-C2"));
		agenda.añadir(new Tarea(new Fecha(14, 5, 2018), "EI1008-C3"));
		System.out.println("Agenda con " + agenda.cantidad() + " tareas");
		System.out.println(agenda);

		agenda.añadir(new Tarea(new Fecha(23, 4, 2018), "EI1010"));
		System.out.println("Agenda con " + agenda.cantidad() + " tareas");
		System.out.println(agenda);
		
		System.out.println("Consulta de 23/04/2018");
		Tarea[] tareas = agenda.consultar(new Fecha(23, 4, 2018));
		for (Tarea t : tareas)
			System.out.println(t.getDescripción());
		
		//agenda.borrarPasadas(new Fecha(20, 4, 2018));
		agenda.borrar();
		System.out.println("Agenda con " + agenda.cantidad() + " tareas");
		System.out.println(agenda);
		
	}

}

package practica3.ejercicio01.a;

public class activitat10 {

	public static void main(String[] args) throws ExcepcionFechaInvalida{
		Agenda agenda =new Agenda();
		Tarea tarea = new Tarea(new Fecha(1,2,2000),"Hola");
		Tarea tarea2 = new Tarea(new Fecha(12,3,1994),"Examen");

		agenda.añadir(tarea);
		agenda.añadir(tarea2);
		agenda.añadir(tarea2);
		agenda.añadir(tarea2);
		agenda.añadir(tarea2);
		agenda.añadir(tarea2);
		agenda.añadir(tarea2);

		System.out.println(agenda);
		System.out.println(agenda.consultar(new Fecha(1,2,1995)));
		System.out.println("Borrando...");
		agenda.borrarPasadas(new Fecha(2,2,1999));
		System.out.println(agenda);
		
	}


	

}

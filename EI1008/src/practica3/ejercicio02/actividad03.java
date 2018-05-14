package practica3.ejercicio02;

public class actividad03 {
	public static void main(String[] args) {
		 ListaCadenasEnlaceSimple node = new ListaCadenasEnlaceSimple();
		//ListaCadenasEnlaceDoble node = new ListaCadenasEnlaceDoble();

		System.out.println("Llistat de talles:\n" + node);
		node.add(0,"Empresas");
		node.add(0,"ARQ");
		node.add(0,"EST");
		node.add(0,"PRO");
		node.add(0,"FISICA");
		node.add(0,"ADE");
		node.add(0,"FUT");
		
		System.out.println("Llistat de talles:\n" + node);
		//node.remove("FUT");
		//System.out.println("Llistat de talles:\n" + node);
		System.out.println(node.ifaddString("Empresas"));
		System.out.println("Llistat de talles:\n" + node);

		

	}

}

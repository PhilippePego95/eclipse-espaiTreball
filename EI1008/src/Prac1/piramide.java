package Prac1;

public class piramide {
	public static void main(String[] args) {
		piramides();
		piram(5);
	}

	public static void piram(int n) {

		for (int i = 1; i <= 5; i++) {
			for (int k = 1; k < n; k++) {
				System.out.print(" ");
			}
			for (int j = 0; j < i; j++) {
				System.out.print("*");
			}
			for (int j = 1; j < i; j++) {
				System.out.print("*");
			}

			System.out.println();
			n--;
		}

	}

	public static void piramides() {
		for (int i = 1; i <= 5; i++) {
			for (int j = 1; j <= i; j++) {
				System.out.print(j);
			}
			System.out.println();
		}
	}

}

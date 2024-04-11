public class NumerosDivisiveisPor5 {
    public static void main(String[] args) {
        System.out.println("Números entre 1000 e 2000 que ao serem divisíveis por 5 produzem resto 3:");

        for (int i = 1000; i <= 2000; i++) {
            if (i % 5 == 3) {
                System.out.println(i);
            }
        }
    }
}

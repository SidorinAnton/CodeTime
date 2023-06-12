package demo;

public class Variables {
    public static void main(String[] args) {
        int intVar = 10;
        double doubleVar = 10.1;
        String stringVar = "Hello!";
        System.out.println(intVar);
        System.out.println(doubleVar);
        System.out.println(stringVar);

        int emptyVar;
        emptyVar = 100;
        System.out.println(emptyVar);

        int a = 1, b = 2, c = 3;
        System.out.println(" " + a + b + c);

        final double PI = 3.14;
//        PI++; !! error !!
        System.out.println(PI);
    }
}

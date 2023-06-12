package demo;

public class Operators {

    /*
     demo.Operators:
     1) + - * / % ++ --
     2) ~ & | ^ >> >>> <<
     */


    // 1.0 / 0.0 -> inf
    // -1.0 / 0.0 -> -inf
    // 0.0 / 0.0 -> nan
    // nan != nan

    public static void main(String[] args) {
        int a = 10, b = 1;
        System.out.println(a + b);
        System.out.println(a - b);
        System.out.println(a * b);
        System.out.println(a / b);
        System.out.println(a % b);
        System.out.println(a & b);
        System.out.println(a | b);
        System.out.println(~a);

        int abs_ = Math.abs(-1);
        int max_ = Math.max(10, 20);
        double sqrt_ = Math.sqrt(16);
        double pi = Math.PI;

        String stringAddRes = "Hello" + 123;
    }
}

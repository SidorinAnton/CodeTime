package demo;

public class Types {
    boolean bool = true;  // (< <= > >= == !=) (! && || ^ & |)

    char symbol = 'c';

    // numbers
    byte b = 3;             // -128 ... +128
    short s = 123;          // -2^15 ... +2^15 - 1
    int i = 1234567;        // -2^31 ... +2^31 - 1
    long l = 10_000_000L;   // -2^63 ... +2^63 - 1

    float f = 23.1f;
    double d = 123.2;

    Boolean bool_ = true;  // same for Character, Byte, Short, Integer, Long, Float, Double
    boolean isNan = Double.isNaN(0.0 / 0.0);
}

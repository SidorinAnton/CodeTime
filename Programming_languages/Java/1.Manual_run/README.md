# 1. Java from CLI

1) Create 'Hello.java' file and add:

```java
public class Hello {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Hello! :)");
        }

        for (int i = 0; i < args.length; i++) {
            System.out.println("Hello " + args[i]);
        }
    }
}
```

2) Compile to bytecode (get 'Hello.class' file):

```shell
javac Hello.java
```

3) We can see human-readable format:

```shell
javap -v Hello.class
```

4) Use JVM to run main method

* Don't use '.class'

```shell
java Hello
java Hello Anton Ann
```

5) Use JAR archive

Zip:

```shell
# jar cfe archive_name.jar name_of_main_class classes
jar cfe hello_archive.jar Hello Hello.class
```

See:

```shell
# jar tf archive_name.jar
jar tf hello_archive.jar
```

Unzip:

```shell
# jar xf archive_name.jar
jar xf hello_archive.jar
```

Run from archive:

```shell
java -jar hello_archive.jar
java -jar hello_archive.jar Anton Ann
```


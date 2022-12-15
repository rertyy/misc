public class Mammal extends Animal {
    int age;
    String name;

    Mammal(String name, int age){
        this.name = name;
        this.age = age;
    }

    Mammal() {
        this.name = "cat";
        this.age = 2000;
    }

}
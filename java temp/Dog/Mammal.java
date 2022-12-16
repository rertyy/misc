public class Mammal extends Animal {
    int age;
    String name;
    String desc;
    int year;

    Mammal(String name, int age){ //constructor overloading means with different parameters
        this.name = name;
        this.age = age;
    }

    // Mammal(String name, int year){ //cannot have duplicate method with same arg types
    //     this.name = name;
    //     this.year = year;
    // }

    Mammal(String name, String desc){ //diff arg types is allowed
        this.desc = desc;
    }

    Mammal() {
        this.name = "cat";
        this.age = 2000;
    }

}
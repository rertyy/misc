public class Animal {
    public static void main(String []args) {
        // Dog dogOne = new Dog("rex", 20); //errors out because constructors are not inherited. 
                                            // If a constructor is not defined, an implicit constructor "Dog() {}" is created, which is not parameterised
                                            // So the default values are taken for Dog, which extends Mammal.
        // System.out.println(dogOne.age);

        Dog dogOne = new Dog(); //does not error out
        System.out.println(dogOne.age);

    }
}

	




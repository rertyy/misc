public class Circle {
        
        Circle() {
                this.radius = 10;
        }

        double radius;
        public Circle(double r) {
                this.radius = r;
        }



        public double getRadius(){
                return this.radius;
        }

        public double getArea() {
                return 3.14 * radius * radius;
        }

        public static void main(String[] args) {
        Circle c1 = new Circle(1);
        Circle c2 = new Circle(5);
        Circle c3 = new Circle(100);
        System.out.println("The circle has radius of "
                + c1.getRadius() + " and area of " + c1.getArea());
        System.out.println("The circle has radius of "
                + c2.getRadius() + " and area of " + c2.getArea());
        System.out.println("The circle has radius of "
                + c3.getRadius() + " and area of " + c3.getArea());


        
        System.out.println();
    }
}
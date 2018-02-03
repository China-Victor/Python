public class JavaPrivate {
    public static void main(String args[]) {
        Stu s = new Stu("Victor", 18);
        s.sayPersonalInfo();
        s.sayStuInfo();

        s.setName("Victor Wu");
        s.setAge(20);

        s.sayPersonalInfo();
        s.sayStuInfo();
    }

    public static class Personal{

        String name;

        private int age;

        public Personal(String name, int age){
            super();
            this.name = name;
            this.age = age;
        }

        public void setName(String name){
            this.name = name;
        }

        public void setAge(int age){
            this.age = age;
        }

        public void sayPersonalInfo(){
            System.out.println("personal info : name = " + this.name + ", age = " + age);
        }
    }


    public static class Stu extends Personal{

        private int age;

        public Stu(String name, int age){
            super(name, age);
            this.name = name;
            this.age = age;
        }

        public void setName(String name){
            this.name = name;
        }

        public void setAge(int age){
            this.age = age;
        }

        public void sayStuInfo(){
            System.out.println("stu info : name = " + this.name + ", age = " + age);
        }

    }
}


public class VariableBasic {
    public static void main(String[] args) {
        // 1. 변수 선언
        int studentNum;
        String name;
        double gradeJava;
        double gradeC;
        double avg;

        // 2. 변수 정의(초기화)
        studentNum = 500;
        name = "inmo yang";
        gradeJava = 4.0;
        gradeC = 3.8;
        avg = 0;

        avg = (gradeJava + gradeC) / 2;
        name = "yeeun";
        studentNum = 600;
        System.out.println(avg);
        System.out.println(name);
        System.out.println(studentNum);
        System.out.println(6); // number
        System.out.println("six"); // string
        System.out.println("6");
        System.out.println("6" + "6");
        System.out.println("1111".length()); // 4
        System.out.println(6 + 2);
        System.out.println(6 - 2);
        System.out.println(6 * 2);
        System.out.println(6 / 2);
        System.out.println(Math.PI);
        System.out.println(Math.floor(Math.PI));
    }
}
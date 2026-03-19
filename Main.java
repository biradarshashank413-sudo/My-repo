
//         System.out.println("enter the marks of science");
//         int science=sc.nextInt();
//         System.out.println("enter the marks of kannada");
//         int kannada=sc.nextInt();
//         System.out.println("enter the marks of bio");
//         int bio=sc.nextInt();
//         float percentage =((maths+english+science+kannada+bio)/500.0f)*100;

//         System.out.println("the total percentage is"+percentage);
//     }
// } 
// ------------------------------------------------------
// public class Main{
//     public static void main(String[] args) {
//         Scanner sc=new Scanner(System.in);
//         System.out.println("enter the numbers :");
//         int a=sc.nextInt();
//         int b=sc.nextInt();
//         int c=sc.nextInt();

//         int sum=a+b+c;

//         System.out.println("the sum of the number :"+sum);

//     }
// }
// -------------------------------------------------------------

// public class Main{
//     public static void main(String[] args) {
//         System.out.println("Hello user enter the name :");
//         Scanner sc=new Scanner(System.in);
//         String str=sc.next();
//         System.out.println("hello!" +str+",have a good day!");
//     }
// }

// -------------------------------------------------------------

// public class Main{
//     public static void main(String[] args) {
//         Scanner sc=new Scanner(System.in);

//         System.out.println("enter the kilometer :");
//         float kilometer=sc.nextFloat();
//         System.out.println("the miles is"+kilometer*0.62);

        
//     }
// }

// ----------------------------------------------------------------

// public class Main{
//     public static void main(String[] args) {
//         Scanner sc=new Scanner(System.in);
//         System.out.println("enter the number:");
//         int number=sc.nextInt();
//         for(int i=0;i<11;i++){
//             System.out.println(number+"x"+i+"="+i*number);
//         }
        
//     }
// }

// ------------------------------------------------------------------------

// public class Main{
//     public static void main(String[] args) {
//         int a=4;
//         int b=--a*8;
        
//         System.out.println(b);
//         System.out.println(b>11);
//     }
// }

// ---------------------------------------------------------------------

// public class Main{
//     public static void main(String[] args) {
//         int i=7;
//         int y= ++i *8;
//         System.out.println(y);

//     }
// }

// ---------------------------------------------------------------------

// public class Main{
//     public static void main(String[] args) {
//         Scanner sc=new Scanner(System.in);
//         System.out.println("Enter the number :");
//         int number=sc.nextInt();
//         System.out.println(45>number);
//         System.out.println("user entered number greater");

//     }
// }
// -----------------------------------------------------------------------

// public class Main{
//     public static void main(String[] args) {
//         int a=5;
//         Float b=5.55f;
//         System.out.printf("the value of a ia %d and the value of b is %f",a,b);
//     }
// }

// -------------------------------------------------------------------------

// public class Main{
//     public static void main(String[] args) {
//         // String name="sHAshank";
//         // int value=name.length();
//         // String small=name.toLowerCase();
//         String text="dear <|name|> , thanks a lot !";
//         String tex=text.replace("<|name|>", "shashank");
        
//         System.out.println(tex);


//     }
// }

// -------------------------------------------------------------------

// public class Main{
//     public static void main(String[] args) {
//         float m1,m2,m3;
//         Scanner sc=new Scanner(System.in);
//         System.out.println("enter the marks of maths :");
//         m1=sc.nextInt();
//         System.out.println("enter the marks of phy:");
//         m2=sc.nextInt();
//         System.out.println("enter the marks chemistry:");
//         m3=sc.nextInt();
//         float avg=(m1+m2+m3)/300f*100;
//         System.out.println(avg);

//         if(avg>=40 && m1>=33 && m2>=33 && m3>=33){
//             System.out.println("pass");

//         }
//         else{
//             System.out.println("Fail");
//         }
//     }
// }

// public class Main{
//     public static void main(String[] args) {
//         int var;
//         System.out.println("Enter your age :");
//         Scanner sc=new Scanner(System.in);
//         var =sc.nextInt();

//         switch(var){
//             case 18:
//                 System.out.println("you are going to be adult");
//                 break;
//             case 23:
//                 System.out.println("now are purusing your professional work");
//                 break;
//             case 30:
//                 System.out.println("your married life");
//                 break;
//             default:
//                 System.out.println("enjoy ur life Man");
            

//         }
//     }
// }

// public class Main{
//     public static void main(String[] args) {
//         int a=10;
//         if(a==11){//the only = operator is not is used in condition insted of that we use relational operator like '=='
//         System.out.println("I'm 11");
//         }
//         else{
//             System.out.println("I'm not 11");
//         }
//     }
// }

// public class Main{
//     public static void main(String[] args) {
//         int day;
//         System.out.println("Enter the number :");
//         Scanner sc=new Scanner(System.in);
//         day=sc.nextInt();
//         switch(day){
//             case 1:
//                 System.out.println("Monday");
//                 break;
//             case 2:
//                 System.out.println("Tuesday");
//                 break;
//             case 3:
//                 System.out.println("Wednesday");
//                 break;
//             case 4:
//                 System.out.println("Thursday");
//                 break;
//             case 5:
//                 System.out.println("Friday");
//                 break;
//             case 6:
//                 System.out.println("Saturday");
//                 break;
//             case 7:
//                 System.out.println("Sunday");
//                 break;
//             default:
//                 System.out.println("Invalid Input");

//         }

        
//     }
// }

// public class Main{
//     public static void main(String[] args) {
//         Scanner sc=new Scanner(System.in);
//         System.out.println("enter the wedsite name :");
//         String website=sc.next();

//         if(website.endsWith(".org")){
//             System.out.println("this is an organisational website");
//         }
            
//         else if(website.endsWith(".com")){
//             System.out.println("this url is commerial website");

//         }

//         else{
//             System.out.println("this is indian website ");
//         }
//     }
// }

// public class Main{
//     public static void main(String[] args) {
//         Random rand = new Random();
//         int computer = rand.nextInt(2);  // generates a random number from 0 to 99
//         // System.out.println(computer);
//         Scanner sc=new Scanner(System.in);
//         System.out.println("enter the input :");
//         int user = sc.nextInt();
//         /*rock=1
//         paper=2
//         scissor=3
//          */
//         if (computer==0 && user==0){
//             System.out.println("its draw");
//         }
//         else if (computer==0 && user==1){
//             System.out.println("you win");
//         }
//         else if (computer==0 && user==2){
//             System.out.println("you lose");
//         }
//         else if (computer==1 && user==1){
//             System.out.println("its draw");
//         }
//     }
// }

// public class Main{
//     public static void main(String[] args) {
        // int i=100;
        // while(i<=200){
        //     System.out.println(i);
        //     i++;
        // }
        //---------------------------------------do while
//         int i=15;
//         do {
//             System.out.println(i);
//             i++;
//         } while (i<5);
//     }
// }


public class Main{
    public static void main(String[] args) {
        
        // int n=0;
        for (int i = 9; i > 0; i--) {
            System.out.println(i);
        }
    }
}
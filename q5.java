public class StringOpe
{
    public static void main (String[] args)
    {
        StringBuffer str1 = new StringBuffer("Sneh");  
        System.out.println("Value of str1 before change : " + str1);
        str1.append("Patel");
        System.out.println("Value of str1 after change : " + str1);
        StringBuffer str2 = new StringBuffer("Saurabh");  
        System.out.println("Value of str1 before change : " + str2);
        str2.append("Yadav");
        System.out.println("Value of str1 after change : " + str2);
        System.out.println(" ");
        String str3="Sneh";
        String str4="Saurabh";
        String str5="Sneh";
        System.out.println(str3.equals(str4));
        System.out.println(str3.equals(str5));
        System.out.println(" ");
        String str6="Sneh";
        String str7="Saurabh";
        System.out.println(str6.length());
        System.out.println(str7.length());
        System.out.println(" ");
        String str8="Sneh";
        String str9="Saurabh";
        System.out.println(str8.charAt(2));
        System.out.println(str9.charAt(5));
        System.out.println(" ");
    }
}

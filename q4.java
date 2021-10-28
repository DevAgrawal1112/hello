public class Box{  
  static int volume=30;  
  static class Size{  
   void msg(){
       System.out.println("Volume is " + volume);
       }  
  }  
  public static void main(String args[]){  
  Box.Size b1 = new Box.Size();  
  b1.msg();  
  }  
}  

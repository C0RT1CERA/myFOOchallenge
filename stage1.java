
public class solution {

    public static String solution(String x) {
        // Your code here
        String str = x;
        String alp1 = "abcdefghijklmnopqrstuvwxyz";
        char val;
        int j;
        String result="";
        for(int i = 0; i<str.length(); i++){
            val = str.charAt(i);
            int ascV = (int) val;
            if(!(ascV>=97 && ascV<=122)){
                result += String.valueOf(val);
            }else{
                for(j=1; j<=alp1.length(); j++){
                    if(val == (alp1.charAt(j))){
                        break;
                    }            
                }result += String.valueOf(alp1.charAt(25 - j));
            } 
        }return result;
    }       
    public static void main(String[] args) {
        System.out.println(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"));        
    }
}

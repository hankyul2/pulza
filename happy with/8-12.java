import java.util.*;
class Solution {

    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = {};
        String buf="";
        String buf2="";
        String sum="";
        buf=happy(arr1,n);
        buf2=happy(arr2,n);
        int temp=0;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(buf.charAt(temp)=='0' && buf2.charAt(temp)=='0'){
                    sum+=" ";
                }
                else{
                    sum+="#";
                }
                temp++;
            }
            if(i!=n-1)
            sum+="h";
        }
        System.out.println(sum);
        answer=sum.split("h",n);
        return answer;
    }
    public String happy(int[] arr,int len){
        StringBuffer sb = new StringBuffer();
        String buffer="";
        String result="";
        for(int x:arr){
            buffer="";
            while(x>=2){
                buffer+=Integer.toString(x%2);
                x=x/2;
            }
            buffer+=Integer.toString(x);
            while(buffer.length()<len){
                buffer+="0";
            }
            result+=sb.append(buffer).reverse().toString();
            sb.setLength(0);
        }

        return result;
    }

}
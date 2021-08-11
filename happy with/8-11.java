import java.util.*;

class Solution {
    public String solution(int[][] scores) {
        String answer="";
        int temp=0;
        int temp2=0;
        int sum=0;
        int len=scores[0].length;
        int min=100;
        int max=-1;
        int[] temp3=new int[len];
        int temp4=0;
        while(temp<len){
            sum=0;
            temp4=0;
            temp2=0;
            min=100;
            max=-1;
        for(int i=0; i<len; i++){
            temp2=scores[i][temp];
            sum+=temp2;
            if(min>temp2)
                min=temp2;
            if(max<temp2)
                max=temp2;
        }
        for(int i=0; i<len; i++){
            temp3[i]=scores[i][temp];
        }
            if(min==scores[temp][temp])
                temp4=count(temp3,min);
            if(max==scores[temp][temp])
                temp4=count(temp3,max);
            
        if(temp4==1){
            sum=(sum-scores[temp][temp])/(len-1);
        }
        else{
            sum=sum/len;
        }
            
        if(sum>=90){
                answer+="A";
        }
        else if(sum>=80){
                answer+="B";
        }
        else if(sum>=70){
                answer+="C";
        }
        else if(sum>=50){
                answer+="D";
        }
        else{
                answer+="F";
        }
        
            temp++;
            
        }
        return answer;
        
        
    }
    
    public int count(int[] arr,int m){
        int count=0;
        for(int x:arr){
         
            if(m==x)
                count++;
        }
        return count;
    }
    
}
class Solution {
    public int solution(String dartResult) {
        int answer=0;
        int[] buffer=new int[3];
        char temp;
        int index=-1;
        
        for(int i=0; i<dartResult.length(); i++){
            temp=dartResult.charAt(i);
            
            if('0'<=temp && temp<='9'){
                index++;
                if(dartResult.charAt(i+1)=='0'){
                    buffer[index]=10;
                    i++;
                }
                else
                    buffer[index]=temp-'0';
            }
    
            else{
                if(temp=='S')
                    buffer[index]=(int)Math.pow(buffer[index],1);
                 if(temp=='D')
                    buffer[index]=(int)Math.pow(buffer[index],2);
                 if(temp=='T')
                    buffer[index]=(int)Math.pow(buffer[index],3);
                if(temp=='*'){
                    if(index>=1){
                        buffer[index]=buffer[index]*2;
                        buffer[index-1]=buffer[index-1]*2;
                    }
                    else
                        buffer[index]=buffer[index]*2;
                }
                if(temp=='#')
                        buffer[index]=buffer[index]*(-1);
            }   
        }
        for(int x: buffer){
            answer+=x;
        }
    
        return answer;
    }
}
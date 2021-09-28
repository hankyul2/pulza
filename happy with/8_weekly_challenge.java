class Solution {
    public int solution(int[][] sizes) {
        //sizes중 가장 큰 값 구하기
        //[a,b] 둘 중 작은 값 배열에 넣고 그 중 가장 큰 값 구하기
        int big=1;
        int small_big=1;
        for(int i=0; i<sizes.length; i++){
            if(big<sizes[i][0])
                big=sizes[i][0];
            if(big<sizes[i][1])
                big=sizes[i][1];
            if(sizes[i][0]>sizes[i][1]){
                if(small_big<sizes[i][1])
                    small_big=sizes[i][1];
            }
            else{
                if(small_big<sizes[i][0])
                    small_big=sizes[i][0];
            }
        }
        
        return big*small_big;
    }
}
import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int len=nums.length;
        Arrays.sort(nums);
        int temp=-1;
        int count=0;
        for(int x:nums){
            if(temp!=x){
                temp=x;
                count++;
            }
        }
        if(count>len/2)
            return len/2;
        else
            return count;
    }
}
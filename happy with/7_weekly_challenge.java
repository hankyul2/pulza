
import java.util.*;

public class Pro_7 {
	
	public static int[] solution(int[] enter, int[] leave) {
		//leave의 첫번쨰가 나타낼때까지 enter 입장, 나타나면
		//leave 인덱스에 남은 member수 ++ , 남아있는 member들 인덱스에 ++ 한다.
		HashSet <Integer> room= new HashSet<Integer>();
		
		int index=0;
		int index2=0;
		int[] answer=new int[leave.length];
		for(int i=0; i<answer.length; i++)
			answer[i]=0;
		
		while(index<leave.length) {
			//room에 leave가 없으면 추가
			if(!room.contains(leave[index])) {
				room.add(enter[index2]);
				index2++;		
			}
			else {
				room.remove(leave[index]);
				answer[leave[index]-1]+=room.size();
				for(int i:room) {
					answer[i-1]+=1;
				}
				index++;
			}
		}
		
		
		return answer;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for(int i:solution(new int[] {1,3,2},new int[] {1,2,3})) {
			System.out.println(i);
		}
		
		
	}

}

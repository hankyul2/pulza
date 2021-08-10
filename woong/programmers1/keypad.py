def solution(numbers, hand):
    leftLocate=[3,0]
    rightLocate=[3,2]
    answer = ''
    
    for i in range(len(numbers)):
        if numbers[i]==1 or numbers[i]==4 or numbers[i]==7:
            answer+='L'
            if(numbers[i]==1):
                leftLocate=[0,0]
            
            elif (numbers[i]==4):
                leftLocate=[1,0]
            
            else :
                leftLocate=[2,0]   
            
         
        elif numbers[i]==3 or numbers[i]==6 or numbers[i]==9:
            answer+='R'
            if numbers[i]==3:
                rightLocate=[0,2]
            
            elif numbers[i]==6: 
                rightLocate=[1,2]
            
            else:
                rightLocate=[2,2]
         
        else:
            leftDist=0
            rightDist=0
            
            if numbers[i]==2:
                leftDist=leftLocate[0]+1-leftLocate[1]
                rightDist=rightLocate[0]+rightLocate[1]-1
                if leftDist>rightDist:
                    answer+='R'
                    rightLocate=[0,1]
                elif leftDist<rightDist:
                    answer+='L'
                    leftLocate=[0,1]
                else :
                    if hand=='left' :
                        answer+='L'
                        leftLocate=[0,1]
                    else:
                        answer+='R'
                        rightLocate=[0,1]           

            elif numbers[i]==5:
                leftDist=abs(1-leftLocate[0])+abs(1-leftLocate[1])
                rightDist=abs(1-rightLocate[0])+abs(1-rightLocate[1])
                if leftDist>rightDist:
                    answer+='R'
                    rightLocate=[1,1]
                elif leftDist<rightDist:
                    answer+='L'
                    leftLocate=[1,1]
                else :
                    if hand=='left' :
                        answer+='L'
                        leftLocate=[1,1]
                    else:
                        answer+='R'
                        rightLocate=[1,1] 

            elif numbers[i]==8:
                leftDist=abs(2-leftLocate[0])+abs(1-leftLocate[1])
                rightDist=abs(2-rightLocate[0])+abs(1-rightLocate[1])
                if leftDist>rightDist:
                    answer+='R'
                    rightLocate=[2,1]
                elif leftDist<rightDist:
                    answer+='L'
                    leftLocate=[2,1]
                else :
                    if hand=='left' :
                        answer+='L'
                        leftLocate=[2,1]
                    else:
                        answer+='R'
                        rightLocate=[2,1] 

            else:
                leftDist=abs(3-leftLocate[0])+abs(1-leftLocate[1])
                rightDist=abs(3-rightLocate[0])+abs(1-rightLocate[1])
                if leftDist>rightDist:
                    answer+='R'
                    rightLocate=[3,1]
                elif leftDist<rightDist:
                    answer+='L'
                    leftLocate=[3,1]
                else :
                    if hand=='left' :
                        answer+='L'
                        leftLocate=[3,1]
                    else:
                        answer+='R'
                        rightLocate=[3,1]              
    
    return answer
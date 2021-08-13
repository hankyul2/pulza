def solution(dartResult):
    answer = 0
    dartSet = []
    answerList = []
    
    while len(dartResult)!=0:
        if dartResult[1]=='0':
            dartResult='a'+dartResult[2:]
        
        if len(dartResult)>=3:
            if dartResult[2]=='*' or dartResult[2]=='#':
                dartSet.append(dartResult[0:3])
                dartResult=dartResult[3:]
            else :
                dartSet.append(dartResult[0:2])
                dartResult=dartResult[2:]
        else:
            dartSet.append(dartResult[0:2])
            dartResult=''
    
    for i in range(len(dartSet)):
        if dartSet[i][0]=='a':
            dartCount=10
        else:
            dartCount=int(dartSet[i][0])

        if dartSet[i][1]=='S':
            answerList.append(dartCount)
        elif dartSet[i][1]=='D':
            dartCount*=dartCount
            answerList.append(dartCount)
        else:
            dartCount*=dartCount*dartCount
            answerList.append(dartCount)
    
    for j in range(len(answerList)):
        if len(dartSet[j])>2:
            if dartSet[j][2]=='*':
                if j==0:
                    answerList[j]=answerList[j]*2
                else:
                    answerList[j-1]=answerList[j-1]*2
                    answerList[j]=answerList[j]*2
            else:
                answerList[j]=-answerList[j]
    
    for k in range(len(answerList)):
        answer+=answerList[k]
                
    return answer

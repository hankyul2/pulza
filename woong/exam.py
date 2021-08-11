def solution(scores):
    answer = ''
    for i in range(len(scores[0])):
        sortScore = column(scores, i)
        sortScore.sort()
        count = len(scores[0])
        avg= 0
        tmp=0
        for j in range(len(scores[0])):
            tmp +=scores[j][i]
            if i==j:
                if (sortScore[0]==scores[j][i] or sortScore[-1]==scores[j][i]) and sortScore.count(scores[j][i])==1:
                    tmp-=scores[j][i]
                    count -=1
                    
        avg = float(tmp)/float(count)  
        if avg >=90:
            answer+='A'
        elif avg<90 and avg>=80:
            answer+='B'
        elif avg<80 and avg>=70:
            answer+='C'
        elif avg<70 and avg>=50:
            answer+='D'
        else:
            answer+='F'
            
    return answer

def column(matrix, i):
    return [row[i] for row in matrix]
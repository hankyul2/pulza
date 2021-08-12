def solution(n, arr1, arr2): 
    answer = []
    numAns = []
    for i in range(n):
        numTemp1 = binary(arr1[i])
        numTemp2 = binary(arr2[i])
        entireStr =''
        if len(numTemp1)<n:
            while len(numTemp1)<n:
                numTemp1.append(0)
                continue
        if len(numTemp2)<n:
            while len(numTemp2)<n:
                numTemp2.append(0)
                continue
        numTemp1.reverse()
        numTemp2.reverse()

        for l in range(n):
            entire = numTemp1[l]+numTemp2[l]
            entireStr +=str(entire)
            
        numAns.append(entireStr)
    

    for j in range(n):
        answerStr=''
        for k in range(n):
            if int(numAns[j][k])>=1:
                answerStr+='#'
            else :
                answerStr+=' '
        answer.append(answerStr)
        
    return answer 
    
def binary(num):
    arr = []
    if num==1 or num==0:
        arr.append(num)
    else:
        while num>1:
            arr.append(num%2) 
            num=int(num/2)
            if num <=1:
                arr.append(num)
            continue

    return arr
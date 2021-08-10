def solution(s):
    answer = s
    words =["zero","one","two","three","four","five","six","seven","eight","nine"]
    numb =["0","1","2","3","4","5","6","7","8","9"]

    
    for word in words:
        for i in range(len(numb)):
            if words[i]==word:
                answer = answer.replace(word,numb[i])
                
    answerI=int(answer)
    return answerI

print(solution("1one"))
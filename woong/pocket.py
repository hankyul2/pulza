def solution(nums):
    answer = 0
    numsSet= set(nums)
    numsList = list(numsSet)
    
    if len(numsList)>= len(nums)/2:
        answer = len(nums)/2
    else :
        answer = len(numsList)
    return answer
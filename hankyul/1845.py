def solution(nums):
    answer = 0
    digit_list = [0 for _ in range(200001)]
    for num in nums:
        if digit_list[num] == 0:
            digit_list[num] += 1
            answer += 1
    answer = answer if answer < (len(nums) / 2) else len(nums)/2 
    return answer

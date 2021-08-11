def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


def solution(scores):
    answer = ''
    scores = [[scores[j][i] for j in range(len(scores))] for i in range(len(scores))]
    for i in range(len(scores)):
        unique = True
        my_val = scores[i][i]
        for j in range(len(scores[i])):
            if my_val == scores[i][j] and i!=j:
                unique = False
                break
        if unique and (max(scores[i]) == my_val or min(scores[i]) == my_val):
            score = (sum(scores[i]) - my_val ) / (len(scores[i])-1)
        else:
            score = sum(scores[i]) / len(scores[i])
        answer += get_grade(score)
    return answer

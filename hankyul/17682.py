import re

def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T':3}
    points = []
    for iter, (g, b, o) in enumerate(re.findall('([0-9]+)(S|D|T)(\*|\#)?', dartResult)):
        points.append(pow(int(g), bonus[b]))
        if o == '*':
            if iter == 0:
                points[0] *= 2
            else: 
                points[iter] *= 2
                points[iter-1] *= 2
        elif o == '#':
            points[iter] = -points[iter]
    answer = sum(points)
    return answer

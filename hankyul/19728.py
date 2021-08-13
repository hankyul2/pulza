import collections

def solution(priorities, location):
    answer = start = 0
    v = priorities[location]
    d = collections.deque([(p, i) for i, p in enumerate(priorities)])
    while len(d):
        if d[0][0] == max(d, key=lambda x: x[0])[0]:
            answer += 1
            if location == d.popleft()[1]:
                break
        else:
            d.rotate(-1)
    return answer

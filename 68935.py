def solution(n):
    answer = 0
    q, r = n, 0
    three = []
    while q != 0:
        q, r = divmod(q, 3)
        three.insert(0, r)
    n = len(three)
    i = 1
    while n:
        answer += three.pop(0) * i
        i *= 3
        n -= 1
    return answer


solution(125)

def solution(n):
    t = ''
    while n!=0:
        t += str(n%3)
        n = n//3
    return int(t, 3)

print(solution(125))

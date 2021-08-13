def solution(progresses, speeds):
    Q = []
    for prog, sped in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((prog-100)//sped):
            Q.append([-((prog-100)//sped), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]

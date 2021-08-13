import math
def solution(progresses, speeds):
    answer = []
    mday = 0
    ndist = 0
    for prog, sped in zip(progresses, speeds):
        rday = math.ceil((100-prog) / sped)
        print(rday)
        if rday <= mday:
            ndist+=1
        else:
            mday = rday
            if ndist != 0:
                answer.append(ndist)
            ndist=1
    answer.append(ndist)
    return answer

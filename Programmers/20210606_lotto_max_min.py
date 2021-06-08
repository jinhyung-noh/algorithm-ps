def solution(lottos, win_nums):
    zeros = 0
    correct =0
    for i in lottos:
        if i == 0:
            zeros +=1
        elif i in win_nums:
            correct +=1
        else:
            pass
    return list(map(lambda x: min(x,6),[7 - (zeros+correct), 7 - correct]))

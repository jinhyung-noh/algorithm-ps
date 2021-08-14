import sys


def baseball():

    def _strike_ball(guess: int, num: int):
        if num == None:
            return
        # strikes = [None] * 3
        strikes = 0
        balls = 0

        # count strikes
        for i in range(3):
            if guess[i] == num[i]:
                # strikes[i] = num[i]
                strikes += 1

        # count balls
        for i in range(3):
            if guess[i] in (num[0:i] + num[i+1:]) :
                balls += 1
                
        return str(strikes), str(balls)
    
    # candidates = list(map(str, range(100, 1000)))
    candidates = []
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i != j and j != k and k != i:
                    candidates.append(str(i)+str(j)+str(k))

    # input queries
    queries = []
    n = int(sys.stdin.readline())
    for _ in range(n):
        queries.append(sys.stdin.readline().split()) 

    for query in queries:
        for i in range(9*8*7):
            if (query[1], query[2]) != _strike_ball(query[0], candidates[i]):
                candidates[i] = None 

    cnt = 0
    for candidate in candidates:
        if candidate != None:
            cnt += 1
    print(cnt)


baseball()
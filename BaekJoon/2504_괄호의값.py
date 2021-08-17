import sys


def parenthesis():

    def _is_VPS():

        stack = []
        for i in range(N):
            if string[i] == ')' and stack and stack[-1] == '(':
                stack.pop()
                continue
            if string[i] == ']' and stack and stack[-1] == '[':
                stack.pop()
                continue
            else:
                stack.append(string[i])
        if stack:
            return False
        return True
                


    def _recur():
        curr = string[idx[0]]
        if curr == '(':
            pair = ')'
            const = 2
        else:
            pair = ']'
            const = 3

        # base case
        if idx[0] < N - 1 and string[idx[0]+1] == pair:
            idx[0] += 1
            if pair == ')':
                return 2
            return 3

        result = 0
        while idx[0] < N - 1 and string[idx[0]+1] != pair:
            idx[0] += 1
            result += _recur()
        
        idx[0] += 1
        return const * result

    # input
    string = sys.stdin.readline().strip()
    N = len(string)

    if not _is_VPS():
        return 0
    
    idx = [-1]
    result = 0
    while idx[0] < N - 1:
        idx[0] += 1
        result += _recur()

    return result

print(parenthesis())

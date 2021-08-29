import sys

def combination(N: int, r: int) -> list[list[int]]:

    if r >= N:
        print("impossible!")
        return

    def _dfs(level: int, curr: int):

        if r >= N:
            print("impossible!")
            return
        
        # base case
        if level == r:
            result.append(route[:])
            return
        
        # recursive call
        for next in range(curr+1, N+1):
            route.append(next)
            _dfs(level+1, next)
            route.pop()
        return

    result = []
    route = []
    for start in range(1, N+1):
        route.append(start)
        _dfs(1, start)
        route.pop()
    return result

def permutation(N: int, r: int) -> list[list[int]]:

    def _dfs(level, curr):

        # base case
        if level == r:
            result.append(route[:])
            return

        # recursive call
        for next in range(1, N+1):
            if next not in route:
                route.append(next)
                _dfs(level+1, next)
                route.pop()
        
    result = []
    route = []
    for start in range(1, N+1):
        route.append(start)
        _dfs(1, start)
        route.pop()
    return result

# print(combination(2, 3))
print(permutation(3, 3))
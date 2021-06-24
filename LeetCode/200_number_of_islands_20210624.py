# using recursion, DFS
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        import sys
        sys.setrecursionlimit(90000)
        m, n = len(grid), len(grid[0])
        cnt = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    cnt += 1
                    self._markIslands(grid, x, y)
        return cnt

    def _markIslands(self, grid, x, y):
        try:
            if x >= 0 and y >= 0 and grid[x][y] == '1':
                grid[x][y] = 'x'
                # clockwise
                for new_x, new_y in [(x-1,y), (x,y+1), (x+1,y), (x,y-1)]:
                    self._markIslands(grid, new_x, new_y)
        except IndexError:
            pass

# using iteration, DFS
class Solution2:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    cnt += 1
                    self._markIslands(grid, x, y)

        return cnt

    def _markIslands(self, grid, x, y):
        S = []  # stack
        S.append((x, y))
        while S != []:
            x, y = S.pop()
            if grid[x][y] == '1':
                grid[x][y] = 'x'
                for new_x, new_y in [(x,y-1), (x+1,y), (x,y+1), (x-1,y)]:
                    # to avoid index error
                    if new_x >=0 and new_x < len(grid) \
                        and new_y >=0 and new_y < len(grid[0]):
                        S.append((new_x, new_y))


# solution in Book
class Solution3:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(i, j):
            # terminate when island over
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                    return None
            
            # marking island
            grid[i][j] = '0'

            # search 4 ways
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
    
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1
        return count






grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution2().numIslands(grid))
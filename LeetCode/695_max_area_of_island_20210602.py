class Solution:
    """
    input : list of list
    output : integer
    """
    def maxAreaOfIsland(self, grid):
        islands = self._maxAreaOfIslandHelper(grid)
        maxval = 0
        for island_list in islands.values():
            area = len(island_list)
            if area > maxval:
                maxval = area
        return maxval
    """
    return hashmap of islands;
    {island identifier : [list of island grids; tuple (i, j)]
    """
    def _maxAreaOfIslandHelper(self, grid):
        
        m = len(grid)
        n = len(grid[0])
        island_dict = {}
        cnt_new_island=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if not self._checkConnection(i, j, grid):   # no connection ; new island
                        island_dict[cnt_new_island] = [(i,j)]
                        cnt_new_island += 1
                    else:
                        count = 0           # if count > 1 : 합치기
                        connected_island = [] # 연결된 섬 기록
                        for key, val in island_dict.items():
                            if self._checkConnection_island(i, j, val):
                                if count == 0:
                                    island_dict[key].append((i, j))
                                    count +=1
                                    connected_island.append(key)
                                else:
                                    island_dict[connected_island[0]] += val
                                    connected_island.append(key)
                        if len(connected_island) > 1:           # 2개 이상 연결된 경우 합체된거 지운다
                            del island_dict[connected_island[1]]
        return island_dict

    # check whether each grid has connection
    def _checkConnection(self, i, j, grid):
        if i == 0:
            check1 = 0
        else:
            check1 = grid[i-1][j]
        if j == 0:
            check2 = 0
        else:
            check2 = grid[i][j-1]
        return check1 or check2

    def _checkConnection_island(self, i, j, islands):
        if ((i-1, j) in islands) or ((i, j-1) in islands): 
            return True 
        return False


def show_grid(grid):
    for row in grid:
        for col in row:
            if col == 0:
                print(" ", end='')
            else:
                print("O", end='')
        print('')

def show_islands(island_dict, m,n):
    init_grid =[]
    for k in range(m):
        init_grid.append([0]*n) 
    for val in island_dict.values():
        for i, j in val:
            init_grid[i][j] = 1
    show_grid(init_grid)



grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid2 = [[0,0,0],[0,1,0],[1,1,1]]
grid3 = [[0,0,0,0,1,0,1,1,0,0,1,0,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,1,1,0,1,1],[0,1,0,0,0,0,1,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,1,0,1,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1],[1,0,0,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,1,1,1],[0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1],[0,0,0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1],[0,0,1,1,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1],[0,1,0,1,0,0,1,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0],[0,1,0,0,1,1,1,1,0,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,0,1,0],[0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0]]
# print(Solution()._maxAreaOfIslandHelper(grid2))
# print(Solution()._maxAreaOfIslandHelper(grid3))
print(Solution().maxAreaOfIsland(grid3))
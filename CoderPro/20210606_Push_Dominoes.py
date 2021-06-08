class Solution:
    def pushDominoes(self, dominoes):
        max_len = len(dominoes)
        forces = [0] * max_len

        force = 0
        for i in range(max_len):
            if dominoes[i] == 'R':
                force = max_len
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(0, force - 1)       # if '.' case : 전 단계 -1 혹은 
            forces[i] = force

        for i in range(max_len-1, -1, -1):
            if dominoes[i] == 'L':
                force = - max_len
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = min(0, force + 1) 
            forces[i] += force
            
        for i in range(len(forces)):
            if forces[i] > 0:
                forces[i] = 'R'
            elif forces[i] < 0:
                forces[i] = 'L'
            else:
                forces[i] ='.'
        
        return ''.join(forces)

input = '....R...L...R...'
print(Solution().pushDominoes(input))
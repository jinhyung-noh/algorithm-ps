def solution(numbers, hand):
    def get_distance(x, y):
        return abs(x[0]-y[0]) + abs(x[1]-y[1])

    # initialize keypad dict : {num, (coordinate ; x, y)}
    keypad  = {}
    for i in range(1,10):
        keypad[i] = (i-1) // 3, (i-1) % 3
    keypad['*']=(3,0); keypad[0]=(3,1); keypad['#']=(3,2)

    answer = []
    LH = '*'
    RH = '#'
    for num in numbers:
        if num in [1,4,7]:
            state = 'LH'
        elif num in [3,6,9]:
            state = 'RH'
        else:       # num in [0,2,5,8]
            L_dist = get_distance(keypad[LH], keypad[num])
            R_dist = get_distance(keypad[RH], keypad[num])
            if L_dist > R_dist:
                state = 'RH'
            elif L_dist < R_dist:
                state = 'LH'
            else:
                if hand == 'left':
                    state = 'LH'
                else:
                    state = 'RH'
        
        if state == 'LH':
            answer.append('L')
            LH = num
        else:
            answer.append('R')
            RH = num
    return ''.join(answer) 

input = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
main_hand = "left`"
print(solution(input, "left"))
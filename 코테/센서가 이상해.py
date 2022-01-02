def sensor_is_strange():

    def _get_error(sen1, sen2):
        cnt = 0
        idx = 0
        for val_sen2 in sen2:
            target = sen1[idx]

            while val_sen2 > 0:
                if sen1[idx] == target:
                    idx += 1
                    val_sen2 -= 1
                    continue
                # 다른경우 같은 것 나올때까지 탐색
                temp = idx
                while sen1[temp] != target:
                    temp += 1
                # swap
                sen1[idx], sen1[temp] = sen1[temp], sen1[idx]
                cnt += (temp - idx)
                idx += 1
                val_sen2 -= 1
            
        return cnt

    import sys
    input = sys.stdin.readline
    input()
    sen1 = list(map(int, input().split()))
    sen2 = list(map(int, input().split()))
    return print(_get_error(sen1, sen2))

sensor_is_strange()
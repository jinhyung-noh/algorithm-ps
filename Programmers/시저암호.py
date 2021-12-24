s = 'aBz'
n = 4

def solution(s, n):
    result = []
    for case in s:
        if case == ' ':
            result.append(' ')
            continue
        str_to_asc = ord(case)

        if ord('A') <= str_to_asc <= ord('Z'):
            standard = ord('A')
        elif ord('a') <= str_to_asc <= ord('z'):
            standard = ord('a')

        check_case = standard + (((str_to_asc + n) - standard) % 26)
        result.append(chr(check_case))
    result = ''.join(result)
    
    return result

print(solution(s, n))


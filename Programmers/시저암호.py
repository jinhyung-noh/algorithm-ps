s = 'aBz'
n = 4

def solution(s, n):
    result = []
    for case in s:
        if case == ' ':
            result.append(' ')
            continue
        str_to_asc = ord(case)
        standard = ord('A')
        small_standard = ord('a')
        if standard <= str_to_asc <= ord('Z'):
            check_case = standard + (((str_to_asc + n) - standard) % 26)
        elif small_standard <= str_to_asc <= ord('z'):
            check_case = small_standard + (((str_to_asc + n) - small_standard) % 26)
        result.append(chr(check_case))
    result = ''.join(result)
    return result

print(solution(s, n))


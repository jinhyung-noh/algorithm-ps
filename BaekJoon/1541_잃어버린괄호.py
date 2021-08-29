import sys


def lost_parentheses():


    # '+'로 이어진 문자열을 숫자로 인식하여 합산한 결과 반환
    def string2int(string):
        return sum(map(int, string.split('+')))

    # input
    # '-'를 기준으로 나누어 리스트로 만듦
    strings = sys.stdin.readline().strip().split(sep='-')
    # 첫번째는 +값이므로 그대로 저장
    result = string2int(strings[0])

    # 두번째부터는 '-'기준으로 나누었으므로 모두 음수로 취급
    for substring in strings[1:]:
        result -= string2int(substring)

    print(result)

lost_parentheses()



def 팰린드롬만들기():
    import sys
    from collections import Counter

    input_string = sys.stdin.readline().strip()
    # Counter로 개수 세기
    alphabets = Counter(input_string)

    # 팰린드롬 만들기
    # 알파벳 순서대로 구성(2개씩 빼기)
    result = ''
    for key in sorted(alphabets.keys()):
        # 2개씩 빼면서 result 반쪽을 만들기
        while alphabets[key] > 1:
            result += key
            alphabets[key] -= 2
        # alphabets[key] == 0이면 삭제
        if alphabets[key] == 0:
            del alphabets[key]

    # 남아있는 것은 홀수개인 것들
    # 홀수개인 것이 2개 이상이면 실패
    if len(alphabets) > 1:
        print("I'm Sorry Hansoo")
        return 
    # 홀수개인 것이 1개이면 그것 붙여주기
    temp = ''
    if len(alphabets) == 1:
        temp = list(alphabets.keys())[0]
    
    print(result + temp + result[::-1])
    return

팰린드롬만들기()
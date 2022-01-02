def ccj():
    def _compress(s):
        """스택을 통해 날아간 문자를 세는 함수"""
        stack = []  # 문자열 쌓는 공간
        cnt = 0     # 날아간 문자 개수
        for char in s:
            # 스택의 마지막과 같은 경우 패스
            if stack and stack[-1] == char:
                cnt += 1
                continue
            stack.append(char)

        return cnt

    def _change(s):
        """이전것과 같은것 세는 함수"""
        cnt = 0
        idx = 1
        while idx < len(s):
            if s[idx] == s[idx-1]:
                cnt += 1
                idx += 2
                continue
            idx += 1
        return cnt
                
    s = input().strip()
    print(_compress(s), _change(s))
    return

ccj()


    
        
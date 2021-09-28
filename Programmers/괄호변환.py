def solution(p):

    # 괄호에 따라 숫자 부여
    def _plus_minus(idx):
        if p[idx] == '(': return 1
        return -1

    # 옳은 괄호 문자열인지 판단
    def _is_right(l, r):
        cnt = _plus_minus(l)
        l += 1
        while cnt >= 0 and l <= r:
            cnt += _plus_minus(l)
            l += 1

        if cnt < 0: return False 
        return True

    # 스트링의 처음과 마지막을 제거하고 괄호 반전
    def _strip_reverse(l, r):
        l += 1
        r -= 1
        if (l >= r): return ""

        temp_str = ""
        while (l <= r):
            if (p[l] == '('): temp_str += ')'
            else: temp_str += '('
            l += 1
        return temp_str

    # recursive, 전체 동작 함수
    def _helper(l, r):
        # exception case
        if (l >= r): return ""

        m = l
        cnt = _plus_minus(m)
        m += 1

        while cnt != 0 and m <= r:

            cnt += _plus_minus(m)
            m += 1
        
        # u: p[l:m]
        # v: p[m:r]
        # u가 옳은 괄호 문자열인 경우
        if _is_right(l, m-1):
            return p[l:m] + _helper(m, r)
        # u가 옳지 않은 괄호 문자열인 경우
        return '(' + _helper(m, r) + ')' + _strip_reverse(l, m-1)

    l = 0
    r = len(p) - 1

    return _helper(l, r)

p = "(()())()"
# p = ")("
# p = "()))((()"

print(solution(p))
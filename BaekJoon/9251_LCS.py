import sys

def LCS():

    # lcs를 구하기 위해 dp table을 채우는 함수
    def get_lcs_table():
        table = [[0] * (m + 1) for _ in range(n + 1)]

        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = max(table[i][j-1], table[i-1][j])

        return table

    # dp table을 역추적하여 공통문자열을 찾아내는 함수
    def get_lcs():

        n = len(lcs_table) - 1
        m = len(lcs_table[0]) - 1
        lcs = []

        while lcs_table[n][m] > 0 and n > 0 and m > 0:

            # dp table에서 같은 숫자가 안나올때까지 이동
            while lcs_table[n][m-1] == lcs_table[n][m]: m -= 1
            while lcs_table[n-1][m] == lcs_table[n][m]: n -= 1
            # 해당 문자 기록
            lcs.append(s1[n-1])

            # 이 상태에서 좌상향으로 이동
            m -= 1
            n -= 1

        # 역순으로 반환
        return "".join(lcs[::-1])

    # inputs
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()

    n, m = len(s1), len(s2)
    lcs_table = get_lcs_table()
    lcs = get_lcs()
    
    # LCS 길이 출력
    print(lcs_table[n][m])
    # LCS 문자열 출력
    print(lcs)
    return

LCS()


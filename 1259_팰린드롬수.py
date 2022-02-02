def 팰린드롬수():
    import sys
    answers = []

    while True:
        number = sys.stdin.readline().strip()
        if number == '0':
            break
        reverse_number = int(number[::-1])
        if int(number) == reverse_number:
            answers.append("yes")
        else:
            answers.append("no")

    print(*answers, sep="\n")

팰린드롬수()
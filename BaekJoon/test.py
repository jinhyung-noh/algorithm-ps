import sys

input_value = sys.stdin.readline().rstrip()


total_count = 0
raiser_count = 0

previous_ch = '('
stack = []
for ch in input_value:
    if ch == '(':
        if not stack:
            raiser_count = 0
        stack.append(ch)
        previous_ch = ch
    else:
        stack.pop()
        if previous_ch == '(':
            raiser_count += 1
        else:
            total_count += (raiser_count + 1)
        previous_ch = ch

print(total_count)
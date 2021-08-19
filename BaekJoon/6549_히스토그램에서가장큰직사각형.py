import sys

def max_area(histograms: list[int]):

    def _update_max_area():

        idx = stack.pop()
        height = histograms[idx]
        width = i - 1 - stack[-1] if stack else i
        max_area[0] = max(max_area[0], height * width)


    
    N = len(histograms)
    stack = [0]
    max_area = [0]
    for i in range(1, N):
        while stack and histograms[i] <= histograms[stack[-1]]:
            _update_max_area()
        stack.append(i)
    
    # pop remaining stack
    i = N
    while stack:
        _update_max_area()

    return max_area[0]


# inputs
answers = []
test_case = list(map(int, sys.stdin.readline().split()))
while test_case[0] != 0:
    answers.append(max_area(test_case[1:]))
    test_case = list(map(int, sys.stdin.readline().split()))

# outputs
for answer in answers:
    print(answer)

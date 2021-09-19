def solution(n, times):
    low = 0
    high = n * max(times)

    while low < high:
        
        mid = (low + high) // 2
        expected = sum([mid//time for time in times])

        if expected == n:
            break
        elif expected < n:
            low = mid+1
        else:
            high = mid-1

    if low >= high:
        mid = high

    return max([time * (mid // time) for time in times])

n = 1
times = [2, 2]
print(solution(n, times))

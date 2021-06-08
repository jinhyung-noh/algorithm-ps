def solution(nums):
    # prime list under 2997 ; 998+999+1000
    prime_list = []
    for i in range(2,2998):
        n = 0
        for j in prime_list:
            if i % j != 0:
                n += 1
        if n == len(prime_list):
            prime_list.append(i)

    nums.sort()
    n = len(nums)
    result = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (nums[i]+nums[j]+nums[k]) in prime_list:
                    print(f"[{nums[i]},{nums[j]},{nums[k]}]를 이용해서 {nums[i]+nums[j]+nums[k]}을 만들 수 있습니다.")
                    result += 1
    return result

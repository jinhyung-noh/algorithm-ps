def solution(s):
    parsed_list = s.split('}')

    answer = []
    temp_list = []

    # parsing given string to lists
    for candidate in parsed_list:
        candidate = candidate.strip(',')
        candidate = candidate.strip('{')
        if candidate != "":
            temp_list.append(candidate.split(','))


    # sort by length: ascending order
    temp_list.sort(key=lambda x: len(x))
    # fill in answer
    for list_n in temp_list:
        for elem in list_n:
            if elem not in answer:
                answer.append(elem)

    # make each element integer
    return list(map(int, answer))

# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))
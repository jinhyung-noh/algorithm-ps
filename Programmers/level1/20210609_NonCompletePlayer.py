def solution(participant, completion):
    def list2dict(listA):
        result = {}
        for elem in listA:
            if elem not in result:
                result[elem] = 1
            else:
                result[elem] += 1
        return result
    
    dict_part = list2dict(participant)
    dict_comp = list2dict(completion)
    for name in dict_comp:
        if (dict_part[name] not in dict_comp) or (dict_part[name] != dict_comp[name]):
            answer = name
            break
    return answer 


participants = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participants, completion))
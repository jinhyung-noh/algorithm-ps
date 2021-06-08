def solution(n, lost, reserve):
	students = [1] * n
	for i in lost:
		students[i-1] -= 1
	for i in reserve:
		students[i-1] += 1

	for std_num, std_state in enumerate(students):
		if std_state == 0:
			if std_num !=0 and students[std_num-1] == 2:
				students[std_num-1] = 1
				students[std_num] = 1
			elif std_num != len(students)-1 and students[std_num+1] ==2:
				students[std_num+1] = 1
				students[std_num] = 1
			else:
				pass
	return sum(map(lambda x: min(x,1), students))

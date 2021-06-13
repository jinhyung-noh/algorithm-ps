class Solution():
    def reorderLogFiles(self, logs: list) -> list:
        letter_logs = []
        digit_logs = []
        for log in logs:
            if log[-1].isdigit():
                digit_logs.append(log)
            else:
                # make log to list form (to sort)
                log2list = log.split()
                letter_logs.append(log2list)
        # sort by logs / identifier
        letter_logs.sort(key=lambda x: [x[1:], x[0]])
        # make logs to string again
        for i in range(len(letter_logs)):
            letter_logs[i] = ' '.join(letter_logs[i])
        return letter_logs + digit_logs


# solution in book ; similar..?
class Solution2:
    def reorderLogFiles(self, logs: list) -> list:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits



        return None
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

print(Solution2().reorderLogFiles(logs))
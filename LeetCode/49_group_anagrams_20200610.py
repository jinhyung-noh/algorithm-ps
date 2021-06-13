# Time limit exceeded solution
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import Counter

        answer = []
        for word in strs:
            # if go through all thw "answer" : new answer!
            count = 0
            for i in answer:
                if Counter(word) == Counter(i[0]):
                    i.append(word)
                    break
                count += 1
            if count == len(answer):
                answer.append([word])

        return answer

# time limit exceeded!
class Solution2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import Counter

        answer = []
        for word in strs:
            # if go through all thw "answer" : new answer!
            # answer = [[Counter(), elem1, elem2, ...], ...[]]
            count = 0
            for i in answer:
                if Counter(word) == i[0]:
                    i.append(word)
                    break
                count += 1
            if count == len(answer):
                answer.append([Counter(word), word])
        return [words[1:] for words in answer]


# sort each word -> add to dictionary
class Solution3:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict
        # anagram_dict = {"ordered_word" : [words]}
        anagram_dict =  defaultdict(lambda : [])
        for word in strs:
            ordered_word = ''.join(sorted(word))
            anagram_dict[ordered_word].append(word) 
        
        return list(anagram_dict.values())
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution3().groupAnagrams(strs))
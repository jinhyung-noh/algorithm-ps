class Solution:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        from collections import Counter
        import re
        # lower case -> replace [!?\',;.] to ' ' -> make list(split)
        listed_paragraph = re.sub('[!?\',;.]',' ',paragraph.lower()).split()
        hash = Counter(listed_paragraph)
        
        # delete keys in banned
        for banned_word in banned:
            if banned_word in hash:
                del hash[banned_word]
                
        # order by occurance -> return the first key value
        return hash.most_common()[0][0]


# solutino in book
class Solution2:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        import collections
        import re                          # \w : alphabet and numbers
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                if word not in banned]
        # hash map {key : counted_numbers}
        counts = collections.Counter(words)
        # return the most common word - first index
        return counts.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"] 

print(Solution2().mostCommonWord(paragraph, banned))
       
       
       
       
       
       
def solution(begin, target, words):
    from collections import deque

    # 바뀌는 것이 가능한지 알아보는 함수
    def _changable(word1, word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
        if cnt == 1:
            return True
        return False

    # BFS using queue
    q = deque()
    for word in words:
        if _changable(begin, word):
            q.append([word])

    while q:
        curr = q.popleft()
        # 탈출조건
        if curr[-1] == target:
            return len(curr)
        
        # 다음 단어가 가능하면 큐에 넣는다
        for next in words:
            if next not in curr and _changable(curr[-1], next):
                q.append(curr + [next])
    
    # 모든 탐색이 끝나면 0 반환
    return 0


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))

   
def solution(answers):

    supo_1 = [1,2,3,4,5];
    supo_2 = [2,1,2,3,2,4,2,5];
    supo_3 = [3,3,1,1,2,2,4,4,5,5];
    ans_cnt = [0,0,0]; # answ_cnt[i-1]: i번째 수포자의 정답 개수

    # answer를 돌면서 각각 정답 확인
    for idx in range(len(answers)):
        answer = answers[idx]
        # 1번 수포자 정답 체크
        if supo_1[idx % 5] == answer:
            ans_cnt[0] += 1
        # 2번 수포자 정답 체크
        if supo_2[idx % 8] == answer:
            ans_cnt[1] += 1
        # 3번 수포자 정답 체크
        if supo_3[idx % 10] == answer:
            ans_cnt[2] += 1

    # 가장 많이 맞힌 사람 확인
    result = []
    max_score = max(ans_cnt)
    for i in range(3):
        if ans_cnt[i] == max_score:
            result.append(i+1)
    
    return result

    
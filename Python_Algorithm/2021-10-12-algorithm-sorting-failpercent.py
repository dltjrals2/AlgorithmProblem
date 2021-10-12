def solution(N, stages):
    answer = []
    answer_dict = dict()
    for i in range(1, N+1):
        total_player = 0
        not_clear_player = 0
        for stage in stages:
            if stage >= i:
                total_player += 1
            if stage == i:
                not_clear_player += 1
        calc = 0 if total_player == 0 else not_clear_player / total_player
        answer.append((i, calc))

    answer = sorted(answer, key = lambda t : t[1], reverse = True)
    answer = [i[0] for i in answer]
    return answer
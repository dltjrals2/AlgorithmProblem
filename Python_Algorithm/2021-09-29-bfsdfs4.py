# 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
def balance(w):
    count = 0
    for i in range(len(w)):
        if w[i] == "(":
            count += 1
        else:
            count -= 1

        if count == 0:
            return i


def proper(w):
    count = 0
    for i in w:
        if i == "(":
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def solution(w):
    answer = ""
    # 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if w == "":
        return answer
    index = balance(w)
    u = w[:index + 1]
    v = w[index + 1:]
    if proper(u):
        answer = u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)
    return answer
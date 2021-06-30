def solution(clothes):
    set = {};
    sum = 1
    for i, j in clothes:
        if set.get(j) == None:
            set[j] = 2
        else:
            set[j] += 1
    for i, j in set.items():
        sum *= j
    sum -= 1
    answer = sum

    return answer

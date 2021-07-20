def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(len(numbers)):
            if i == j:
                continue
            else:
                if numbers[i]+numbers[j] not in answer:
                    answer.append(numbers[i]+numbers[j])
    answer = sorted(answer)
    return answer

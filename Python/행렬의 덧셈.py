def solution(arr1, arr2):
    answer = []
    temp = []
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append([])
        for j in range(len(arr1[0])):
            answer[i].append(temp[j])
        temp.clear()
    return answer

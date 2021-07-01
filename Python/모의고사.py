def solution(answers):
    answer = []
    n = len(answers)
    
    first = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    arr1 = []
    arr2 = []
    arr3 = []
    
    for i in range(1, n+1):
        if i % 10 != 0:
            arr1.append(first[i % 10 - 1])
            arr3.append(third[i % 10 - 1])
        else:
            arr1.append(first[9])
            arr3.append(third[9])
        if i % 8 != 0:
            arr2.append(second[i % 8 - 1])
        else:
            arr2.append(second[7])
            
    one = 0
    two = 0
    three = 0
    
    for i in range(0, n):
        if arr1[i] == answers[i]:
            one += 1
        if arr2[i] == answers[i]:
            two += 1
        if arr3[i] == answers[i]:
            three += 1
            
    if one == two and two == three:
        answer = [1, 2, 3]
    elif one == two:
        if one > three:
            answer = [1, 2]
        else:
            answer = [3]
    elif two == three:
        if two > one:
            answer = [2, 3]
        else:
            answer = [1]
    elif three == one:
        if two > one:
            answer = [2]
        else:
            answer = [1, 3]
    elif one > two and one > three:
        answer = [1]
    elif two > one and two > three:
        answer = [2]
    else:
        answer = [3]

    return answer

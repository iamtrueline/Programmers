def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)
    left = 0
    right = len(people)-1
    
    while people[left] > limit/2 and right-left> 0:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            answer += 1
        else:
            left += 1
            answer += 1
    if right-left > 0:
        answer += (int)((right-left+1)/2) + (right-left+1)%2
    else:
        answer += 1
    
    return answer

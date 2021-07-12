def solution(nums):
    answer = 0
    n = len(nums)/2
    sort = []
    
    for i in range(len(nums)):
        if nums[i] not in sort:
            sort.append(nums[i])
            if len(sort)>= n:
                return n
    if n < len(sort):
        answer = n
    else:
        answer = len(sort)
    
    return answer

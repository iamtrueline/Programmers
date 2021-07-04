rlt = 0

def search(numbers, target, dep, num):
    if dep == len(numbers):
        if num == target:
            return 1
        return 0   
    ans = 0
    num += numbers[dep]
    ans += search(numbers, target, dep+1, num)
    num -= numbers[dep]
    num -= numbers[dep]
    ans += search(numbers, target, dep+1, num)
    return ans
    

def solution(numbers, target):
    answer = 0
    
    answer = search(numbers, target, 0, 0)
    
    return answer

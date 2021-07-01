def chk(chklist, rltlist, dep, tmp):
    if dep == len(chklist):
        return
    else:
        for i in range(len(chklist)):
            if chklist[i][1] != 1:
                tmp= tmp + chklist[i][0]
                chklist[i][1] = 1
                if int(tmp) not in rltlist:
                    rltlist.append(int(tmp))
                chk(chklist, rltlist, dep + 1, tmp)
                tmp= tmp[:-1]
                chklist[i][1] = 0
    return

def isprime(number):
    if number == 1 or number == 0:
        return False
    n = number**(1/2)
    for i in range(2, int(n) + 1):
        if number%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    chklist = []
    rltlist = []
    
    
    for i in range(len(numbers)):
        chklist.append([numbers[i], 0])
    
    chk(chklist, rltlist, 0, '')
    for i in range(len(rltlist)):
        if isprime(int(rltlist[i])):
            answer += 1
    
    return answer

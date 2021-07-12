def solution(s):
    answer = ''
    block = 0
    
    for i in range(len(s)):
        if block != 0:
            block -= 1
            continue
        if ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
            answer += s[i]
        else:
            if s[i] == '-':
                continue
            if s[i] == 'z':
                answer += '0'
                block = 3
            elif s[i] == 'o':
                answer += '1'
                block = 2
            elif s[i] == 't':
                if s[i+1] == 'w':
                    answer += '2'
                    block = 2
                else:
                    answer += '3'
                    block = 4
            elif s[i] == 'f':
                if s[i+1] == 'o':
                    answer += '4'
                    block = 3
                else:
                    answer += '5'
                    block = 3
            elif s[i] == 's':
                if s[i+1] == 'i':
                    answer += '6'
                    block = 2
                else:
                    answer += '7'
                    block = 4
            elif s[i] == 'e':
                answer += '8'
                block = 4
            elif s[i] == 'n':
                answer += '9'
                block = 3
    
    return int(answer)

def solution(s):
    answer = ''
    arr = []
    for i in range(len(s)):
        arr.append(ord(s[i]))
    arr = sorted(arr, reverse=True)
    for i in range(len(s)):
        answer += chr(arr[i])
    return answer

def solution(arr):
    bang = sorted(arr, reverse=True)
    little = bang[-1]
    listt = []
    for i in range(len(arr)):
        if arr[i] == little:
            listt.append(i)
    for i in range(len(listt)-1, -1, -1):
        arr.pop(listt[i])
    if len(arr) == 0:
        arr.append(-1)
    return arr

def solution(n, arr1, arr2):
    answer = []
    st = ""
    for i in range(len(arr1)):
        arr1[i] = str(bin(arr1[i]))
        arr2[i] = str(bin(arr2[i]))
        arr1[i] = arr1[i][2:]
        arr2[i] = arr2[i][2:]
        while len(arr1[i])<n or len(arr2[i])<n:
            if len(arr1[i])<n:
                arr1[i] = "0" + arr1[i]
            if len(arr2[i])<n:
                arr2[i] = "0" + arr2[i]
        
        for j in range(len(arr1[i])):
            if arr1[i][j]=="0" and arr2[i][j]=="0":
                st += " "
            else:
                st += "#"
        answer.append(st)
        st = ""
    return answer

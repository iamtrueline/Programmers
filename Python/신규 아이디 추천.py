def solution(new_id):
    answer = ''
    valid = ['-', '_', '.', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    deletelist = []
    new_id = new_id.lower()
    
    new_id = list(new_id)
    for i in range(len(new_id)):
        if new_id[i] not in valid:
            deletelist.append(i)
    deletelist = sorted(deletelist, reverse = True)
    for i in range(len(deletelist)):
        new_id.pop(deletelist[i])
    deletelist.clear()
                    
    for i in range(1, len(new_id)):
        if new_id[i-1] == '.' and new_id[i] == '.':
            deletelist.append(i-1)
    deletelist = sorted(deletelist, reverse = True)
    for i in range(len(deletelist)):
        new_id.pop(deletelist[i])
    deletelist.clear()
    
    if new_id[0] == '.':
        new_id.pop(0)
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id.pop(-1)
        
    if len(new_id) == 0:
        new_id.append('a')
        
    while len(new_id) >= 16:
        new_id.pop()
        if new_id[-1] == '.':
            new_id.pop(-1)
    
    while len(new_id) < 3:
        new_id.append(new_id[-1])

    answer = "".join(new_id)
    
    return answer

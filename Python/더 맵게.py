import heapq

def solution(scoville, K):
    answer = 0
    ispass = False
    
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    
    while len(heap)>1 and ispass == False:
        if heap[0] >= K:
            ispass = True
            break
        else:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
            answer += 1
            if heap[0] >= K:
                ispass = True
    if ispass == False:
        return -1
    
    return answer

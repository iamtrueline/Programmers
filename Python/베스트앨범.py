def solution(genres, plays):
    answer = []
    genres_rank = {}
    genres_play = {}
    
    for i in range(len(genres)):
        if genres_rank.get(genres[i]) == None:
            genres_rank[genres[i]] = plays[i]
            genres_play[genres[i]] = [[plays[i], i]]
        else:
            genres_rank[genres[i]] += plays[i]
            genres_play[genres[i]].append([plays[i], i])

    
    sorted_genres_rank = sorted(genres_rank.items(), key=lambda x: x[1], reverse=True)

    
    for gen in sorted_genres_rank:
        genres_play_sub = genres_play[gen[0]]
        genres_play_sub = sorted(genres_play_sub, reverse=True) 
        
        
        for i in range(len(genres_play_sub)):
            if i == 2:
                break
            if len(genres_play_sub)-1 > i:
                if genres_play_sub[i][0] == genres_play_sub[i+1][0] and genres_play_sub[i][1] > genres_play_sub[i + 1][1]:
                    temp = genres_play_sub[i][1]
                    genres_play_sub[i][1] = genres_play_sub[i + 1][1]
                    genres_play_sub[i + 1][1] = temp
            answer.append(genres_play_sub[i][1])
                
    
    return answer

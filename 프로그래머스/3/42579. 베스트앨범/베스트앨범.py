def solution(genres, plays):
    answer = []
    
    keys = set(genres)
    genres_order = {key: 0 for key in keys}
    genres_plays = {key: [] for key in keys}
    
    for i, (genre, cnt) in enumerate(zip(genres, plays)):
        genres_order[genre] += cnt
        genres_plays[genre].append((i, cnt))
        
    for genre, _ in sorted(genres_order.items(), key = lambda x: x[1], reverse = True):
        for i, cnt in sorted(genres_plays[genre], key = lambda x: x[1], reverse = True)[:2]:
            answer.append(i)
    
    return answer
def solution(friends, gifts):
    gift_record = [[0] * len(friends) for _ in range(len(friends))]  # 선물 기록
    receive_record = {name: 0 for name in friends}  # 받은 기록
    gift_score = {name: 0 for name in friends}  # 선물 지수
    friends_dict = {}  # 인덱스 저장
    
    # 인덱스 저장 딕셔너리 초기화
    for idx, name in enumerate(friends):
        friends_dict[name] = idx
    
    # 선물 주고받은 내역 저장
    for record in gifts:
        giver, receiver = record.split()
        giver_idx, receiver_idx = friends_dict[giver], friends_dict[receiver]
        gift_record[giver_idx][receiver_idx] += 1
        receive_record[receiver] += 1
        
    print(gift_record)
    
    for i in range(len(friends)):
        gift_score[friends[i]] = sum(gift_record[i]) - receive_record[friends[i]]
    
    print(gift_score)
    
    result = [0] * len(friends)
    for friend in friends:
        friend_idx = friends_dict[friend]
        for i in range(friend_idx, len(friends)):
            if gift_record[friend_idx][i] > gift_record[i][friend_idx]:
                result[friend_idx] += 1
            elif gift_record[friend_idx][i] < gift_record[i][friend_idx]:
                result[i] += 1
            else:
                if gift_score[friend] > gift_score[friends[i]]:
                    result[friend_idx] += 1
                elif gift_score[friend] < gift_score[friends[i]]:
                    result[i] += 1
                else:
                    continue
        
    return max(result)
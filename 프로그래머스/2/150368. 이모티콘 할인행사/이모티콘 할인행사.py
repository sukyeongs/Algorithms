from itertools import product

def solution(users, emoticons):
    answer = [0, 0]  # answer[0]: 최대 가입자, answer[1]: 최대 판매액
    
    emoticon_price = []  # emoticon_price: 각 이모티콘 할인별 가격 2차원 리스트
    for price in emoticons:
        emoticon_price.append([(10, int(price // 10 * 9)), (20, int(price // 10 * 8)), (30, int(price // 10 * 7)), (40, int(price // 10 * 6))])
    
    for case in product(*emoticon_price):
        join = 0
        money = 0
        
        for user in users:
            tmp_money = sum([c[1] for c in case if c[0] >= user[0]])
            if tmp_money >= user[1]:
                join += 1
            else:
                money += tmp_money
        
        if answer[0] < join or (answer[0] == join and answer[1] < money):
            answer = [join, money]
    
    return answer
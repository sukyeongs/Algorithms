# 81301 - Lv.1 숫자 문자열과 영단어

def solution(s):
    answer = s
    num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven":7, "eight":8, "nine":9, "zero":0}
    for items in num_dict.items():
        answer = answer.replace(items[0], str(items[1]))

    return int(answer)
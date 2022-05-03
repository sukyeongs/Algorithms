# 72410 - Lv.1 신규 아이디 추천

def solution(new_id):
    # 1단계 - 소문자로 치환
    new_id = new_id.lower()
    answer = ''
    special_text = {'-', '_', '.'}

    # 2단계 - 알파벳 소문자, 숫자, 허용 특수문자만 남기기
    for c in new_id:
        if c.isalnum() or c in special_text:
            answer += c

    # 3단계 - 마침표 2개 이상 연속 -> 1개로 수정하기
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계 - 처음이나 끝에 오는 마침표 지우기
    answer = answer.strip('.')

    # 5단계 - 빈 문자열이면 a 대입하기
    if len(answer) == 0:
        answer += 'a'

    # 6단계 - 문자열 길이가 16자 이상이면 첫 15자만 남기기
    if len(answer) >= 16:
        answer = answer[:15]

    # 지우고 난 후 끝이 마침표면 없애기
    answer = answer.rstrip('.')

    # 7단계 - 문자열 길이가 2자 이하라면 3자가 될 때까지 마지막 글자 붙이기
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[len(answer) - 1]

    return answer
def solution(new_id):
    new_id = new_id.lower()  # 소문자 치환
    answer = ''
    special_text = {'-', '_', '.'}  # 남길 특수 문자
    
    # 소문자, 숫자, 특정 특수 문자 제외 제거
    for id in new_id:
        if id.isalnum() or id in special_text:
            answer += id
    
    # 마침표 2번 이상 연속된 부분 하나로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 처음이나 끝에 위치한 마침표 제거
    answer = answer.strip('.')

    # 빈 문자열이면 a 대입
    if len(answer) == 0:
        answer += 'a'

    # 16자 이상이면 앞에서부터 15개의 문자만 남김
    if len(answer) >= 16:
        answer = answer[:15]
    
    # 제거 후 마침표가 끝에 위치하면 제거
    answer = answer.rstrip('.')

    # 2자 이하면 길이가 3이 될 때까지 마지막 문자 끝에 붙임
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[len(answer)-1]
    
    return answer
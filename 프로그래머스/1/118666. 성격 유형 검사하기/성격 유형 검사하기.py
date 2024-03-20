def solution(survey, choices):
    answer = ''
    
    score_dict = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    result_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for index, question in enumerate(survey):
        disagree, agree = question[0], question[1]
        if choices[index] <= 3:
            result_dict[disagree] += score_dict[choices[index]]
        elif choices[index] >= 5:
            result_dict[agree] += score_dict[choices[index]]
        else:
            continue
    
    if result_dict['R'] >= result_dict['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if result_dict['C'] >= result_dict['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if result_dict['J'] >= result_dict['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if result_dict['A'] >= result_dict['N']:
        answer += 'A'
    else:
        answer += 'N'
    
    return answer
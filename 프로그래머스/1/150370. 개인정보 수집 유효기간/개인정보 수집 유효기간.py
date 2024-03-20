def date_to_day(date, m):
    year, month, day = map(int, date.split("."))
    month += m
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    
    term_dict = {}
    for term in terms:
        term_type, term_period = term.split()
        term_dict[term_type] = int(term_period)

    today_day = date_to_day(today, 0)
    for index, privacy in enumerate(privacies):
        privacy_date, term = privacy.split()
        expired_day = date_to_day(privacy_date, term_dict[term])
        
        if expired_day <= today_day:
            answer.append(index + 1)
            
    return answer
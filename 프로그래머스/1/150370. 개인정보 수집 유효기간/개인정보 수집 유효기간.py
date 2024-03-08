def time_to_day(date):
    y, m, d = map(int, date.split('.'))
    return y * 12 * 28 + m * 28 + d


def solution(today, terms, privacies):
    answer = []
    terms_period = {}
    
    for term in terms:
        term_type, period = term.split()
        terms_period[term_type] = int(period) * 28
        
    for index, privacy in enumerate(privacies):
        date, term = privacy.split()
        if time_to_day(date) + terms_period[term] <= time_to_day(today):
            answer.append(index + 1)

    return answer
# 92334 - Lv.1 신고 결과 받기

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    result = set(report)
    result = list(result)

    report_dic = {}
    for id in id_list:
        report_dic[id] = []

    for i in result:
        reporter, reported = i.split()
        report_dic[reported].append(reporter)

    for key, value in report_dic.items():
        if len(value) >= k:
            for person in value:
                answer[id_list.index(person)] += 1

    return answer
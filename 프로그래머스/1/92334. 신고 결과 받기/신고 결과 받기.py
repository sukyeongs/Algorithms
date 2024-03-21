def solution(id_list, report, k):
    answer = []
    
    report_dict = {key: set() for key in id_list}  # 각 유저별 신고한 유저 저장
    cnt_dict = {key: 0 for key in id_list}  # 신고 받은 횟수 저장
    
    for r in report:
        reporter, reportee = r.split()
        if reporter in report_dict and reportee in report_dict[reporter]:
            continue
        else:
            report_dict[reporter].add(reportee)
            cnt_dict[reportee] += 1
        
    
    stop = {id for id in id_list if cnt_dict[id] >= k}
    print(stop)
    
    for reporter, reportee in report_dict.items():
        answer.append(len(reportee.intersection(stop)))
        
    return answer
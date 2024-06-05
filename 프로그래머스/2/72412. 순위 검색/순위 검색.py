def solution(info, query):
    data = dict()
    for lang in ['cpp', 'java', 'python', '-']:
        for job in ['backend', 'frontend', '-']:
            for career in ['junior', 'senior', '-']:
                for soul_food in ['chicken', 'pizza', '-']:
                    data.setdefault((lang, job, career, soul_food), list())

    for i in info:
        i = i.split()
        for lang in [i[0], '-']:
            for job in [i[1], '-']:
                for career in [i[2], '-']:
                    for soul_food in [i[3], '-']:
                        data[(lang, job, career, soul_food)].append(int(i[4]))

    for k in data:
        data[k].sort()

    answer = list()

    for q in query:
        q = q.split()
        scores = data[(q[0], q[2], q[4], q[6])]
        wanted = int(q[7])
        l, r = 0, len(scores)
        
        while l < r:
            middle = (l + r)//2
            if scores[middle] >= wanted:
                r = middle
            else:
                l = middle + 1
        answer.append(len(scores)-l)
        
    return answer
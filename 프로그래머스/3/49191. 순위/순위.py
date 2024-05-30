def solution(n, results):
    answer = 0
    record = {i + 1: [set(), set()] for i in range(n)}

    for result in results:
        record[result[0]][0].add(result[1])
        record[result[1]][1].add(result[0])

    for _ in range(2):
        for i in record.keys():
            for wins in record[i][0]:
                record[i][0] = record[i][0].union(record[wins][0])

            for loses in record[i][1]:
                record[i][1] = record[i][1].union(record[loses][1])

    for i in record.keys():
        if len(record[i][0]) + len(record[i][1]) == n - 1:
            answer += 1

    return answer
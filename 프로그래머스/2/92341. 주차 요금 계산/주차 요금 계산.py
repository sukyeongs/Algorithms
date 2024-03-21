import math

def time_to_minute(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def solution(fees, records):
    answer = []
    
    current = {}
    car_list = []
    total_minute = {}
    
    for record in records:
        time, car, state = record.split()
        if car not in current:
            current[car] = [time]
            car_list.append(car)
        else:
            current[car].append(time)

    for key, value in current.items():
        if len(value) % 2 != 0:
            current[key].append('23:59')

    for car, record in current.items():
        total_minute[car] = 0
        for i in range(0, len(record), 2):
            total_minute[car] += time_to_minute(record[i+1]) - time_to_minute(record[i])
    
    car_list.sort()
    
    for car in car_list:
        total = total_minute[car]
        if total <= fees[0]:
            answer.append(fees[1])
        else:
            total -= fees[0]
            answer.append(fees[1] + fees[3] * math.ceil(total/fees[2]))
    
    return answer
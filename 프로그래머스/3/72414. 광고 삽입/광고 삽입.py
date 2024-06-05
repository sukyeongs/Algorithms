def convert_time_to_sec(time):
    h, m, s = map(int, time.split(":"))
    return h * 60 * 60 + m * 60 + s


def solution(play_time, adv_time, logs):
    play_time = convert_time_to_sec(play_time)   
    adv_time = convert_time_to_sec(adv_time)
    record = [0 for _ in range(play_time + 1)]

    for log in logs:
        start, end = map(convert_time_to_sec, log.split("-"))
        
        record[start] += 1
        if end == play_time:
            continue
        record[end] -= 1

    for i in range(1, len(record)):
        record[i] += record[i-1]
    
    for i in range(1, len(record)):
        record[i] += record[i-1]
        
    cur = record[adv_time - 1]
    start_time = 0
    for t in range(adv_time, play_time):
        if cur < record[t] - record[t - adv_time]:
            cur = record[t] - record[t-adv_time]
            start_time = t - adv_time + 1
	
    s = str(start_time % 60).zfill(2)
    m = str(start_time // 60 % 60).zfill(2)
    h = str(start_time // 60 // 60).zfill(2)

    return h + ":" + m + ":" + s
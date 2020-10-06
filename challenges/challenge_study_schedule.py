def study_schedule(start_time, end_time, target_time):
    count = 0
    if target_time < 0 or target_time > 23:
        return count
    for idx, values in enumerate(start_time):
        if (target_time >= start_time[idx] and target_time <= end_time[idx]):
            count += 1
    return count


start_time = [4, 1, 3, 2]
end_time = [4, 3, 4, 5]
target_time = 4
print(study_schedule(start_time, end_time, target_time))

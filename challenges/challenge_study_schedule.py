def study_schedule(start_time, end_time, target_time):
    counter = 0
    for item in range(len(start_time)):
        if start_time[item] <= target_time <= end_time[item]:
            counter += 1
    return counter


start_time = [4, 1, 3, 2]
end_time = [4, 3, 4, 5]
target_time = 2
print(study_schedule(start_time, end_time, target_time))

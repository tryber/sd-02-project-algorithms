def study_schedule(start_time, end_time, target_time):
    counter = 0

    for index in range(len(start_time)):
        if start_time[index] <= target_time <= end_time[index]:
            counter += 1

    return counter


start_time = []
end_time = []
target_time = 0
print(study_schedule(start_time, end_time, target_time))

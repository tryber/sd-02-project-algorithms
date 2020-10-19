def study_schedule(start_time, end_time, target_time):
    counter = 0

    for index, _ in enumerate(start_time):
        if start_time[index] <= target_time <= end_time[index]:
            counter += 1

    return counter


start_time = []
end_time = []
target_time = 0
print(study_schedule([4, 1, 3, 2], [4, 3, 4, 5], 0))

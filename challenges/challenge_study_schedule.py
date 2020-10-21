def study_schedule(start_time, end_time, target_time):
    dict1 = {}
    maximum = 0
    for ind, _ in enumerate(range(len(start_time))):
        for j in range(start_time[ind], end_time[ind] + 1, 1):
            if j in dict1:
                dict1[j] += 1
            else:
                dict1[j] = 1
            if dict1[j] > maximum:
                maximum = j
    return maximum


start_time = [2, 1, 2, 1, 4, 4]
end_time = [2, 2, 3, 5, 5, 5]
target_time = 0

print(study_schedule(start_time, end_time, target_time))

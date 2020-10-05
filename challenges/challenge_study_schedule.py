def study_schedule(start_time, end_time, target_time):
    acumulador = 0
    for index in range(len(start_time)):
        if target_time >= start_time[index] and target_time <= end_time[index]:
            acumulador += 1
    return acumulador


start_time = []
end_time = []
target_time = 0
print(study_schedule(start_time, end_time, target_time))

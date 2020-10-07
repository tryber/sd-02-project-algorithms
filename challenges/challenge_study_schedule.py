def study_schedule(start_time, end_time, target_time):
    total_students = 0
    for time in range(len(start_time)):
        if target_time >= start_time[time] and target_time <= end_time[time]:
            total_students += 1
    return total_students
    # Faça o código aqui.


start_time = [2, 1, 2, 1, 4, 4]
end_time   = [2, 2, 3, 5, 5, 5]
target_time = 2
print(study_schedule(start_time, end_time, target_time))

'''
    Número de estudantes estudando no mesmo horário
    maior quantidade de pessoas acessando o conteúdo da plataforma ao mesmo tempo
    qual é o melhor horário para disponibilizar os materiais de estudo
    valores diferentes para a variável `target_time`, analisando o retorno da função.
'''

# O(n)
def study_schedule(start_time, end_time, target_time):
    count = 0
    for index, value in enumerate(start_time):
        if target_time >= value and target_time <= end_time[index]:
            count += 1
    return count

def best_hour(start_time, end_time, time_length):
    study_quantity = 0
    current_hour = []
    for time in range(0, time_length + 1):
        quantity = study_schedule(start_time, end_time, time)
        if study_quantity < quantity:
            study_quantity = quantity
            current_hour = [time]
        elif study_quantity == quantity:
            current_hour.append(time)

    return current_hour


start_time = [2, 1, 2, 1, 4, 4]
end_time = [2, 2, 3, 5, 5, 5]

print(best_hour(start_time, end_time, 5))


start_time = [4, 1, 3, 2]
end_time = [4, 3, 4, 5]

print(best_hour(start_time, end_time, 5))

# print(best_hour(time_length))

'''
número de estudantes (0, 1 , n)
let count

target_time 0 

iterar sobre start_time 
    se maior ou igual:
        consultar o end_time(start_time_index)
            se maior:
                pass
            se menor ou igual:
                count += 1
            
    se menor:
        pass

se count == 0

'''
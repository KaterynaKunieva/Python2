# # ВАРІАНТ 8(7)
# # ЗАВДАННЯ 1
try:  
    x = int(input('Введіть x = '))
    alpha = int(input('Введіть альфа = '))
    beta = int(input('Введіть бета > альфа = '))
    gamma = int(input('Введіть гама > бета = '))
    if beta <= alpha: 
        raise Exception('бета <= альфа')
    if gamma <= beta: 
        raise Exception('гама <= бета')
except ValueError as ve:
    print(f'Допущена помилка: {ve}')
except Exception as e: 
    print(f'При вводі допущена помилка: {e}')
else: 
    print(f'Всі значенні введені вірно: x = {x}, alpha = {alpha}, beta = {beta}, gamma = {gamma}. Починаю обчислення.')
    if x<=alpha: 
        S = 0
    elif alpha <= x <= beta: 
        try: 
            S = 2*((x-alpha)/(gamma-alpha))**2
        except ZeroDivisionError as z: 
            print(f'Помилка обчислень: {z}')
    elif beta <= x <= gamma: 
        try: 
            S = 1-2*((x-gamma)/(gamma-alpha))**2
        except ZeroDivisionError as z: 
            print(f'Помилка обчислень: {z}')
    elif x >= gamma: 
        S = 1
    print(f'S = {S}')

# ЗАВДАННЯ 2
N = -1
while N<3 or N>9: 
    try: 
        N = int(input('Ведіть N від 3 до 9 включно: '))
        if N<3: 
            raise Exception('Значення N менше 3')
        if N>9: 
            raise Exception('Значення N більше 9')
    except Exception as e: 
        print(f'Невірно введено число: {e}')
    else: 
        print(f'Значення N введено вірно: {N}')       
        for row in range(2, N+2): 
            arr = [] 
            a = 0
            for i in range(1, row):
                a+=1
                arr.append(i)
            a-=1
            for j in range(a, 0, -1):
                arr.append(j) 
            strarr = ' '.join(map(str, arr))
            print(strarr.center(N*4))
        # або: 
        # for i in range(1, N+1): 
        #     for j in range(N+1-i): 
        #         print(" ", end = " ")
        #     for j in range (1, i): 
        #         print(j, end = " ")
        #     for i in range(i, 0, -1): 
        #         print(i, end = " ")
        #     print("")
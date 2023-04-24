# ВАРІАНТ 8 

# 0 
n = 250 
for i in range(n): 
    if i**2 <= n: 
        print(i)

# 1.7 (згідно варіанту)
j = 10  
i = 0
c = 0
while i < j: 
    i = int(input(f'Введіть число менше {j}: '))
    c += 1
else: 
    c -= 1
print(f'Упс! Ви ввели число, яке більше або дорівнює {j}. Кількість правильно введених чисел: {c}')

# 2.3 (згідно варіанту)
start = 1
end = 90
sum = 0 
for i in range(start, end+1): 
    if not i%2: 
        sum+=1 
print(f'Сума всіх непарних числе діапазону від {start} до {end} дорівнює {sum}')

# 2.6 (згідно варіанту)
print('Таблиця множення на 9')
for i in range(1, 10): 
        print(f'{i} x 9 = {i*9}')

# 2.16 (згідно варіанту)
a = int(input('Введіть число а = '))
b = int(input('Введіть число b = '))
sum = 0 
for i in range(a, b+1): 
    sum += i
print(f'Сума всіх цілих чисел діапазону від {a} до {b} дорівнює {sum}')

# 3.1A (згідно варіанту)
# функція визначення місяця: 
def m(i): 
    months = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень']
    if i > 12:
        j = i-13
        month = months[j]
        year = 2021
    else: 
        month = months[i-1]
        year = 2020
    return month, year
sum = 1000
perc = 0.02
# цикл: 
for i in range(3, 16): 
    step = 0
    step = sum*perc
    sum += step
    month, year = m(i)
    print(f'{month} - {step:.2f}')
    if step > 30: 
        print(f'Величина щомісячного збільшення вкладу перевищить 30 грн у {month} {year} р.')
        break

# 3.2 (згідно варіанту)
import random as r
start = 3 
rate = 1 
fail = 0 
win = 0 
n = 1
select = ['Орел', 'Решка']

while start > 0: 
    print(f'Раунд {n}')
    choice = int(input('Введіть 0, якщо випаде орел. Введіть 1, якщо випаде решка. Ваш варіант - '))
    if choice in (1, 0): 
        n += 1
        chance = r.randint(0, 1)
        print(select[chance])
        if choice == chance: 
            win += 1
            start += rate 
            res = 'Ура! Ви вгадали!'
        else: 
            fail += 1 
            start -= rate
            res = 'Упс! Ви програли!'
        statistica = f'Кількість виграшів - {win} \nКількість програшів - {fail} \nСтан рахунку - {start} грн'
        print(res)
        print(statistica)
        answer = input('Продовжити?') 
        if answer == '': 
            continue
        else: 
            start = -1
    else: 
        res = f'Гра завершена! Стан рахунку - {start} грн'
        print(res)
        break
else: 
    res = f'Гра завершена!'
    print(res)
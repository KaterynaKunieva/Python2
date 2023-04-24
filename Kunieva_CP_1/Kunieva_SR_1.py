import creditcalc as cc

# функція для обробки запроса суми кредита, перевірка на додатність і коректність введенних даних 
def get_cred_amount():
    a = 0
    count = 0
    while a <= 0:
        if (count != 0): print('Помилка! Ви ввели некоректні дані. Спробуйте ще раз. ')
        count+=1
        try:
            a = float (input ('Введіть суму кредиту: '))
        except:    
            a = 0
    return a

# функція для обробки запроса терміну кредита, перевірка на додатність і ціле число 
def get_cred_months():
    a = 0
    count = 0
    while a <= 0:
        if (count != 0): print('Помилка! Ви ввели некоректні дані. Спробуйте ще раз. ')
        count+=1
        try:
            a = int (input ('Введіть термін кредиту в місяцях: '))
        except:    
            a = 0
    return a

# функція для обробки запроса проценту кредита, перевірка на додатність і коректність введенних даних 
def get_cred_percent():
    a = 0
    count = 0
    while a <= 0:
        if (count != 0): print('Помилка! Ви ввели некоректні дані. Спробуйте ще раз. ')
        count+=1
        try:
            a = float (input ('Введіть відсоток, під який берете кредит: '))
        except:    
            a = 0
    return a

# функція для обробки запроса типу кредитних платежів, перевірка відповідності введених даних 1 або 0
def get_cred_type():
    a = -1
    count = 0
    while a not in (0, 1):
        if (count != 0): print('Помилка! Ви ввели некоректні дані. Спробуйте ще раз. ')
        count+=1
        try:
            a = float (input ('Введіть 0 для диференційованих платежів, введіть 1 для ануїтентних платежів: '))
        except:    
            a = -1
    return a

def print_table(my_tuple): 
    (l, s1, s2) = my_tuple
    header = ['Період', 'Залишок по кредиту', 'Погашення боргу', 'Погашення відсотків', 'Щомісячний платіж']
    print('{0:->10} {1:->20} {2:->20} {3:->20} {4:->20}'.format('|', '|', '|', '|', '|'))
    print('{:^9}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(*header))
    print('{0:->10} {1:->20} {2:->20} {3:->20} {4:->20}'.format('|', '|', '|', '|', '|'))
    for row in l: 
        print('{:^9}|{:^20.2f}|{:^20.2f}|{:^20.2f}|{:^20.2f}|'.format(*row))
    print("\nПереплата по відсотках за кредит - {0} грн".format(s1))
    print("Всього виплат по кредиту - {0} грн".format(s2))


cred_amount = get_cred_amount()
cred_months = get_cred_months()
cred_percent = get_cred_percent() 
cred_type = get_cred_type()
cred_types = {0: 'Диференційований', 1: 'Ануїтетний'}

print(f'{cred_types[cred_type]} графік погашення кредиту')
if cred_type == 0: 
    tab = cc.def_credit(cred_amount, cred_months, cred_percent)
elif cred_type == 1: 
    tab = cc.anu_credit(cred_amount, cred_months, cred_percent)

print_table(tab)
import random as r 
def test(): 
    k = True
    while k: 
        try: 
            x = int(input('Введіть значення: '))
            if x < 0: 
                raise Exception('Помилка! Введіть ціле число!')
        except Exception as e: 
            print(e)
        else:
            return x
def minimal(): 
    print('Мінімальне число у списку')
    a = test()
    return a
def maximal(): 
    print('Максимальне число у списку')
    b = test()
    return b
def number(): 
    print('Кількість чисел у списку')
    c = test()
    return c
def ask(): 
    a = minimal()
    b = maximal()
    c = number()
    rand(a, b, c)
def printdict(dict): 
    for key, value in dict.items(): 
        print(f"'{key}' - {value}")
def rand(a, b, c):
    arr = []
    for i in range(1, c+1):  
        s = r.randint(a, b)
        arr += [s]
    print(f'Список з випадковими цілими числами: {arr}')
    num = []
    for i in arr: 
        num += [arr.count(i)]
    arr = list(tuple(arr))   
    d = dict(zip(arr, num))
    print(f'Словник з випадковими цілими числами та їх кількістю у списку: {d}')
    new = dict(sorted(d.items(), key=lambda x: x[0]))
    print(f'У списку випадкових цілих чисел, числа зустрічаються у такій кількості: ')
    printdict(new)
ask()
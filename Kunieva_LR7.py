# Завдання 1.1 
import math as m
def test(x):
    k = m.floor(x/(2*m.pi))
    if x <= -2*m.pi: 
        x += 2*m.pi*k
    elif 2*m.pi <= x:
        x -= 2*m.pi*k
    return x
def cosinus(x, eps=10**(-10)): 
    cx = test(x)
    cosx = 0.0
    n = 1
    xn = 1 
    while abs(xn)>eps: 
        cosx += xn
        a = (-1)**n
        b = cx**(2*n)
        f = m.factorial(2*n)
        xn = a*(b/f)
        n += 1
    return cosx
try: 
    x = float(input('Введіть значення x в радіанах: '))
except ValueError: 
    print('Невірно введено значення х')
else: 
    r = cosinus(x)
    print(f'Для x = {x:.2f}: ')
    print(f"cos(x) = {r:.2f} - за рядом Тейлора")
    print(f"cos(x) = {m.cos(x):.2f} - перевірка бібліотекою math")

# Завдання 2 
def is_odd(t): 
    if t%2: 
        return True
    elif not t%2: 
        return False
def what(): 
    try: 
        s = int(input('Введіть ціле число: '))
    except Exception: 
        print('Помилка! Ви не ввели ціле число.')
    else: 
        i = is_odd(s)
        print(i)
what()

# Завдання 3 
def is_prime(n): 
    k = 0
    for i in range(2, n): 
        if not n%i: # число не ділиться на жодне з 2 до n, ставимо індикатор і виходимо
            k+=1
            break
    if k: # True (k = 1)
        return False # не просте
    else: 
        return True 
def question(): 
    try: 
        a = int(input('Введіть ціле число: '))
    except: 
        print('Помилка! Ви не ввели ціле число.')
    else: 
        q = is_prime(a)
        print(q)
question()

# Завдання 4
def S(x): 
    sum = 0 
    for i in range(1, 6): 
        s = 0 
        s = (-1)*i*(x/(m.factorial(i)))
        sum += s
    print(sum)
y = int(input('Введіть значення x: '))
S(y)
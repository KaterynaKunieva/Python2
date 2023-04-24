# номер у списку групи - 8

# ЗАВДАННЯ 1 (7 варіант згідно доданого в курсі файла)
x = int(input('x = '))
y = int(input('y = '))
print(not x*y < 0 or y>x) 

# ЗАВДАННЯ 2 (7 варіант згідно доданого в курсі файла)
for X in (True, False): 
    for Y in (True, False): 
        for Z in (True, False): 
            f = not(Y or not (X and Z)) or Z
            print ("{} \t{} \t{} \t{}".format(X, Y, Z, f))

# ЗАВДАННЯ 3 (7 варіант згідно доданого в курсі файла)
x = int(input('X = '))
y = int(input('Y = '))
z = int(input('Z = '))
n = int(input('Кратність: '))
if x%n or y%n or z%n: 
    print(f'Не всі числа кратні {n}.') 
else: 
    print(f'Кожне з чисел кратне {n}.')

# ЗАВДАННЯ 4.1
x = int(input('X = '))
if x>0: 
    Y = 1
elif not x: 
    Y = 0
elif x<0: 
    Y = -1
print('Y =', Y)

# ЗАВДАННЯ 4.4
First = int(input('First = '))
Second = int(input('Second = '))
if First > Second: 
    Result = First - Second 
elif First < Second: 
    Result = First + Second
elif First == Second: 
    Result = f'First = Second = {Second}'
print(Result)

# ЗАВДАННЯ 4.9
a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))
if a>b+c or b>a+c or c>a+b: 
    result = 'Такого трикутника не існує.'
elif a == b and b == c: 
    result = 'Трикутник рівносторонній.'
elif a == b or b == c or a == c: 
    result = 'Трикутник рівнобедрений.'
elif a**2 == b**2 + c**2 or b**2 == a**2+c**2 or c**2 == a**2 + b**2: 
    result = 'Трикутний прямокутний.'
else: 
    result = 'Трикутник різнобічний'
print(result)